from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from apps.home.vistas.settingsUrls import *
from rest_framework import viewsets, permissions
from consultasTango.models import EB_facturaManual
from consultasTango.serializers import facturaManual
from consultasTango.forms import DateForm
from consultasLakersBis.models import Direccionario
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes,parser_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.http import HttpResponse
from datetime import date
from django.utils import timezone
from datetime import timedelta

# from django.shortcuts import render
from django.db.models import Count
# from .models import EB_facturaManual
# from .forms import DateForm

def facturas_por_fecha(request):
    form = DateForm(request.GET)
    suc = Direccionario.objects.filter(canal__in=['PROPIOS', 'EXTERIOR'])
    listSuc = suc.values_list('nro_sucursal', flat=True)
    imagenes_por_sucursal = {}
    facturas_con_imagenes = []
    elemtosSuc =[]

    if form.is_valid():
        date = form.cleaned_data['date']
        facturas = EB_facturaManual.objects.filter(fechaRegistro__date=date).values('numeroSucursal').annotate(count=Count('numeroSucursal'))

        # Obtén las imágenes asociadas a cada factura
        i=1
        fact= len(facturas)
        fact= fact-1
        for factura in facturas:
            numero_sucursal = factura['numeroSucursal']
            imagenes = list(EB_facturaManual.objects.filter(numeroSucursal=numero_sucursal,fechaRegistro__date=date).exclude(imgFactura=None).values_list('imgFactura', flat=True))
            tipoFac = list(EB_facturaManual.objects.filter(numeroSucursal=numero_sucursal,fechaRegistro__date=date).exclude(tipoFactura=None).values_list('tipoFactura', flat=True))
            cant = facturas[fact]['count']
            for i in range(cant):
                elemtosSuc.append((imagenes[i],tipoFac[i]))
                
            imagenes_por_sucursal[numero_sucursal] = dict(elemtosSuc)
            elemtosSuc.clear()
        
        # Obtén el total de imágenes cargadas para cada sucursal
        total_imagenes = {}
        for numero_sucursal in listSuc:
            total_imagenes[numero_sucursal] = len(imagenes_por_sucursal.get(numero_sucursal, {}))
        
        # Agrupa las sucursales y su total de imágenes cargadas
        
        for numero_sucursal in listSuc:
            sucursal = Direccionario.objects.get(nro_sucursal=numero_sucursal)
            facturas_con_imagenes.append((numero_sucursal, total_imagenes.get(numero_sucursal, 0), sucursal.desc_sucursal))
   
    return render(request, 'appConsultasTango/listarFacturasManuales.html', {'form': form, 'facturas': facturas_con_imagenes, 'imagenes_por_sucursal': imagenes_por_sucursal})


@api_view(['GET'])
def login(request):
    username = request.META.get('HTTP_USERNAME')
    password = request.META.get('HTTP_PASSWORD')

    if username is None or password is None:
        return Response({'error': 'Falta proporcionar el nombre de usuario o la contraseña'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Nombre de usuario o contraseña inválidos'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar si el usuario pertenece al grupo "Adm01"
    if not user.groups.filter(name='admin').exists():
        return Response({'error': 'El usuario no pertenece a un grupo autorizado'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar si el usuario está activo
    if not user.is_active:
        return Response({'error': 'El usuario no está activo'}, status=status.HTTP_400_BAD_REQUEST)

    # token_date = date.today().strftime("%Y%m%d")
    if Token.objects.filter(user=user).exists():
        Token.objects.filter(user=user).delete()
    # token = Token.objects.create(user=user)
    # Crear el token
    token = Token.objects.create(user=user)

    # Obtener la fecha y hora actual en la zona horaria del servidor
    current_datetime = timezone.now()

    # Establecer la fecha y hora del token con la fecha y hora actual
    token.created = current_datetime
    token.save()

    return Response({'token': token.key}, status=status.HTTP_200_OK)

from datetime import date
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime, timedelta

from datetime import datetime, timedelta

def validate_token(token):
    vilidateToken = True
    msgError = ''
    try:
        token = Token.objects.get(key=token)
    except Token.DoesNotExist:
        msgError = 'Token inválido'
        vilidateToken = False

    token_date = token.created
    c_dateTime = datetime.now().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    c_date = c_dateTime.date()
    t_date = token_date.date()
    # Calcula la diferencia de tiempo
    diferencia_time = c_dateTime - token_date
    # Convierte la diferencia de tiempo a segundos
    diferencia_segundos = diferencia_time.seconds
    # Calcula la diferencia en horas
    diferencia_horas = diferencia_segundos // 3600
    # Si deseas obtener un valor absoluto (sin signo), puedes usar abs()
    diferencia_horas_abs = abs(diferencia_horas)
    # Finalmente, asigna el valor entero de la diferencia de horas
    diferencia_horas_entero = int(diferencia_horas_abs)

    if t_date != c_date:
        msgError = 'Token expirado'
        vilidateToken = False
    
    if diferencia_horas_entero > 3:
        msgError = 'Token expirado'
        vilidateToken = False

    return vilidateToken,msgError




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getFacturas(request, numSuc):
    user = request.user
    token = request.auth
    vilidateToken, msgError = validate_token(token)
    if vilidateToken == False:
        return Response({'error': msgError}, status=status.HTTP_401_UNAUTHORIZED)

    today = timezone.now().date()
    last_five_days = today - timedelta(days=7)
    facturas = EB_facturaManual.objects.filter(numeroSucursal=numSuc, fechaRegistro__gte=last_five_days)
    serializer = facturaManual(facturas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([JSONParser, MultiPartParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def postFactura(request):
    datos = request.data
    # print(datos)
    # Acceder al archivo adjunto (imagen de factura)
    img_factura = request.FILES.get('imgFactura')
    # return Response({'ok': 'ok'}, status=status.HTTP_200_OK)
    token = request.auth
    vilidateToken, msgError = validate_token(token)
    if vilidateToken == False:
        print('Error al obtener el token')
        return Response({'error': msgError}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = facturaManual(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class uploadFactura(viewsets.ModelViewSet):
#     queryset = EB_facturaManual.objects.all()
#     serializer_class = facturaManual
#     # permission_classes = [permissions.IsAuthenticated]
    

def altaFactura(request,IdSuc):
    return render(request, 'appConsultasTango/altaFactura.html')

