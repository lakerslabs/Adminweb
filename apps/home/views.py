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
from django.views.generic.list import ListView
from apps.home.vistas.viewsDash import *
from apps.home.vistas.viewsReportes import *
from apps.home.vistas.viewsHerramientas import *
from apps.home.vistas.viewsExtras import *



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


