import pprint
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from Transportes.models import Transporte
from Transportes.forms import TransporteForm
from django.views.generic.list import ListView
from apps.home.vistas.settingsUrls import *
from consultasTango.forms import TurnoForm
from consultasTango.models import Turno

# @login_required(login_url="/login/")
# def (request):
#     Nombre=''
#     dir_iframe = DIR_REPORTES['']
#     return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})


# Logistica
@login_required(login_url="/login/")
def Eliminar_Turno(request):
    if request.method == 'POST':
        IdTurno = request.POST.get('IdTurno')
        datos = Turno.objects.get(IdTurno=IdTurno)
        datos.delete()
        # Redirigir a la página de éxito
        return redirect('/../Herramientas/Calendario/TurnoListView')
    else:
        IdTurno = request.GET.get('IdTurno')
        datos = Turno.objects.get(IdTurno=IdTurno)
        return render(request, 'appConsultasTango/Eliminar_turno.html', {'datos': datos})

@login_required(login_url="/login/")
def Editar_Turno(request,IdTurno):
    datos = Turno.objects.get(IdTurno=IdTurno)
    if request.method == 'POST':
        form = TurnoForm(request.POST or None, request.FILES or None, instance=datos)
        if form.is_valid():
            form.save()
            # Redirigir a la página de éxito
            return redirect('/../Herramientas/Calendario/TurnoListView')
    else:
        form = TurnoForm(instance=datos)
    return render(request, 'appConsultasTango/Editar_turno.html', {'form': form})

@login_required(login_url="/login/")
def Listar_turno(request):
    datos = Turno.objects.all()   
    return render(request,'appConsultasTango/turno_list.html', {'turnos': datos})

@login_required(login_url="/login/")
def Crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de éxito
            return redirect('/../Herramientas/Calendario/TurnoListView')
    else:
        form = TurnoForm()
    return render(request, 'appConsultasTango/Crear_turno.html', {'form': form})


@login_required(login_url="/login/")
def Gestion_cronograma(request):
    Nombre = 'Gestión cronograma'
    dir_iframe = DIR_HERAMIENTAS['Gestion_cronograma']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })


@login_required(login_url="/login/")
def Gestion_guias_mayoristas(request):
    Nombre = 'Guías mayoristas'
    dir_iframe = DIR_HERAMIENTAS['Gestion_guias_mayoristas']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })

# Abastecimiento


@login_required(login_url="/login/")
def Stock_excluido(request):
    Nombre = 'Stock excluido'
    dir_iframe = DIR_HERAMIENTAS['Stock_excluido']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })


@login_required(login_url="/login/")
def Carga_de_orden(request):
    Nombre = 'Carga de orden'
    dir_iframe = DIR_HERAMIENTAS['Carga_de_orden']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })


@login_required(login_url="/login/")
def Activar_orden(request):
    Nombre = 'Activar orden'
    dir_iframe = DIR_HERAMIENTAS['Activar_orden']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })


@login_required(login_url="/login/")
def Desactivar_orden(request):
    Nombre = 'Desactivar orden'
    dir_iframe = DIR_HERAMIENTAS['Desactivar_orden']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })

# Comercial
@login_required(login_url="/login/")
def Ventas_sucursales(request):
    Nombre = 'Ventas sucursales'
    dir_iframe = DIR_HERAMIENTAS['Ventas_sucursales']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })

@login_required(login_url="/login/")
def Gestion_categoria_productos(request):
    Nombre = ''
    dir_iframe = DIR_HERAMIENTAS['Gestion_categoria_productos'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def AdministrarCuotas(request):
    Nombre = 'Administrar Cuotas'
    dir_iframe = DIR_HERAMIENTAS['AdministrarCuotas'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

# Mayoristas
@login_required(login_url="/login/")
def Adm_Pedido(request):
    Nombre = 'Adm Pedido'
    dir_iframe = DIR_HERAMIENTAS['Adm_Pedido']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })

# Ecommerce


@login_required(login_url="/login/")
def Control_pedidos(request):
    Nombre = 'Control pedidos'
    dir_iframe = DIR_HERAMIENTAS['Control_pedidos']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })


@login_required(login_url="/login/")
def StockSegVtex(request):
    Nombre = 'Adm. Stock Seguridad Vtex'
    dir_iframe = DIR_HERAMIENTAS['StockSegVtex']
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe, })

# Gerencia
@login_required(login_url="/login/")
def rendircobranzas(request,UserName):
    Nombre = 'Rendir Cobranzas'
    dir_iframe = DIR_HERAMIENTAS['rendircobranzas'] + UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def GestionarCobro(request,UserName):
    Nombre = 'Gestionar Cobro'
    dir_iframe = DIR_HERAMIENTAS['gestionarCobro'] + UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

# Administracion
@login_required(login_url="/login/")
def Controlgastos(request):
    Nombre = 'Control Gastos'
    dir_iframe = DIR_HERAMIENTAS['controlGastos'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def Cargargastos(request):
    Nombre = 'Gestionar Cobro'
    dir_iframe = DIR_HERAMIENTAS['cargaGastos'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def Controlcajasdiario(request):
    Nombre = 'Control cajas Diario'
    dir_iframe = DIR_HERAMIENTAS['Controlcajasdiario'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def CargaGastosAlquileres(request):
    Nombre = 'Carga Gastos Alquileres'
    dir_iframe = DIR_HERAMIENTAS['CargaGastosAlquileres'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def GestionDeAlquileres(request):
    Nombre = 'Gestión % De Alquileres'
    dir_iframe = DIR_HERAMIENTAS['GestionDeAlquileres'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

# Administracion_CE             ***Comercio Exterior***
@login_required(login_url="/login/")
def Cargarcontenedor(request):
    Nombre = 'Cargar Contenedor'
    dir_iframe = DIR_HERAMIENTAS['cargaInicial'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })

@login_required(login_url="/login/")
def EditarContenedor(request):
    Nombre = 'Editar Contenedor'
    dir_iframe = DIR_HERAMIENTAS['mostrarOrden'] #+ UserName
    return render(request, 'home/PlantillaHerramientas.html', {'dir_iframe': dir_iframe,'Nombre':Nombre })



