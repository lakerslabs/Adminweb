# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import pprint
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from Transportes.models import Transporte
from Transportes.forms import TransporteForm
from reservarsala.models import reservaSala
# from reservarsala.form import reservaForm
from django.views.generic.list import ListView



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def direccionario(request):
    dir_iframe = 'http://192.168.0.143:8080/proyecto_21/direccionario/index.php'
    return render(request,'home/direccionario.html',{'dir_iframe':dir_iframe})


@login_required(login_url="/login/")
def transporte(request):
    transportes = Transporte.objects.all()
    return render(request, 'appTransporte/gestionTransporte.html', {'transportes': transportes})

@login_required(login_url="/login/")
def registrarTransporte(request):
    codigo=request.POST['codTransporte']
    nombre=request.POST['nombreTransporte']
    costBulto=request.POST['costBulto']
    costeSeguro=request.POST['costeSeguro']
    costeRetiro=request.POST['costeRetiro']
    costeEntrega=request.POST['costeEntrega']
    retiraBultos=request.POST['retiraBultos']
    notas=request.POST['notas']
    print(codigo + " - " + nombre)

    # transporte = Transporte
    # transporte. COD_TRANSP = codigo
    # transporte. NOMBRE = nombre
    # transporte. COSTE_BULTO = costBulto
    # transporte. COSTE_SEGURO = costeSeguro
    # transporte. COSTE_RETIRO = costeRetiro
    # transporte. COSTE_ENTREGA = costeEntrega
    # transporte. RETIRA_EN_CD = retiraBultos
    # transporte. OBSERVASIONES = notas
    # transporte.save(force_insert=True)

    # Transporte.create(COD_TRANSP=codigo, NOMBRE=nombre, COSTE_SEGURO=costBulto, COSTE_SEGURO=costeSeguro, COSTE_RETIRO=costeRetiro, COSTE_ENTREGA=costeEntrega, RETIRA_EN_CD=retiraBultos, OBSERVASIONES=notas)
    # IntegrityError: UNIQUE constraint failed: m****t.subject_id
    t= Transporte.create(COD_TRANSP=codigo, NOMBRE=nombre, COSTE_BULTO=costBulto, COSTE_SEGURO=costeSeguro, COSTE_RETIRO=costeRetiro, COSTE_ENTREGA=costeEntrega, RETIRA_EN_CD=retiraBultos, OBSERVASIONES=notas)
    # t.save(force_insert=True)
    return redirect('transporte')


@login_required(login_url="/login/")
def crearTransporte(request):
    formulario = TransporteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        transporte = formulario.save(commit=False)
        transporte.save()
        return redirect('transporte')
    return render(request, 'appTransporte/crearTransporte.html', {'formulario': formulario}) 

@login_required(login_url="/login/")
def editarTransporte(request, id):
    transporte=Transporte.objects.get(COD_TRANSP=id)
    formulario = TransporteForm(request.POST or None, request.FILES or None, instance=transporte)
    if formulario.is_valid() and request.POST:
        transporte = formulario.save(commit=False)
        transporte.save()
        return redirect('transporte')
    return render(request, 'appTransporte/editarTransporte.html', {'formulario': formulario}) 


@login_required(login_url="/login/")
def eliminarTransporte(request, id):
    transporte=Transporte.objects.get(COD_TRANSP=id)
    transporte.delete()
    return redirect('transporte') 

@login_required(login_url="/login/")
def reservar(request):
    reserva = reservaSala.objects.all()
    print(reserva.values())
    return render(request, 'appReserva/turnos.html', {'reserva': reserva})


# @login_required(login_url="/login/")
# def reservarTurnos(request):
#     setEventos={
#         'plugins': [ 'bootstrap', 'interaction', 'dayGrid', 'timeGrid' ],
#         'header' : "{left:'prev,next today', center:'title', right:'dayGridMonth,timeGridWeek,timeGridDay'}",
#         "'themeSystem'": "'bootstrap'",
#         # //Random default events
        
#         'events': '',
#         'editable': 'true',
#         'droppable': 'true',
#         'drop': 'function(info) {if (checkbox.checked) {info.draggedEl.parentNode.removeChild(info.draggedEl);}}'
#       }
#     turnos = cargarEventos()
#     # turnos = [turno for turno in reserva.values('fecha_inicio')]
#     # turnos=[]
#     # for turno in reserva:
#     #     turnos.append(turno.fecha_inicio.strftime('%d'))
#     # pprint.pprint(turnos)
#     # print(turnos)
#     setEventos['events'] = turnos
#     # pprint.pprint(setEventos)
#     aux='{'
#     for clave,valor in setEventos.items():
#         aux=aux+clave+' : '+str(valor)+','

#     aux=aux + '}'    
    
#     # aux=str(setEventos)
    
#     # print(type(aux))
#     # print(aux)
#     # print(type(setEventos))
#     return render(request, 'appReserva/calendario.html', {'turnos': aux})

def cargarEventos():
    # turnos=[]
    # eventos={}
    # diccionario={'title':'', 'start':'', 'end':'','backgroundColor':'', 'borderColor':'','allDay':''}
    diccionario={'allDay' : "false",
             'backgroundColor' : "'#f39c12'",
             'borderColor' : "'#f39c12'",
             'end' : 'new Date(2021,12,27,16,00)',
             'start' : 'new Date(2021,12,27,15,00)',
             'title' : "'Sala1'"}
    reserva = reservaSala.objects.all()
    # for turno in reserva:
    #     diccionario['title']=turno.titulo
    #     y=turno.fecha_inicio.strftime("%Y")
    #     m=turno.fecha_inicio.strftime("%m")
    #     d=turno.fecha_inicio.strftime("%d")
    #     h=turno.fecha_inicio.strftime("%H")
    #     mi=turno.fecha_inicio.strftime("%M")
    #     diccionario['start']='new Date('+y+','+m+','+d+','+h+','+mi+')'
    #     y=turno.fecha_fin.strftime("%Y")
    #     m=turno.fecha_fin.strftime("%m")
    #     d=turno.fecha_fin.strftime("%d")
    #     h=turno.fecha_fin.strftime("%H")
    #     mi=turno.fecha_fin.strftime("%M")
    #     diccionario['end']='new Date('+y+','+m+','+d+','+h+','+mi+')'
    #     diccionario['backgroundColor']=turno.backgroundColor
    #     diccionario['borderColor']=turno.borderColor
    #     diccionario['allDay']=turno.allDay
    #     turnos.append(diccionario)
    
    # turnos.append(diccionario)
    turnos='[{'
    for clave,valor in diccionario.items():
        turnos=turnos+clave+' : '+str(valor)+','

    turnos=turnos + '}]'
    return turnos
    

# @login_required(login_url="/login/")
class reservarTurnos2(ListView):
    model = reservaSala
    template_name = 'appReserva/calendario.html'
    # context_object_name = 'reserva'
    def get_queryset(self):
        return reservaSala.objects.all()

@login_required(login_url="/login/")
def reservarTurnos(request):
    reserva = reservaSala.objects.all()
    return render(request, 'appReserva/calendario.html', {'turnos': reserva})