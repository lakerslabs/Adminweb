# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pprint
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from consultasTango.models import StockCentral
from django.views.generic.list import ListView
from apps.home.vistas.settingsUrls import *
from core.filters import *

@login_required(login_url="/login/")
def direccionario(request):
    Nombre='Pedidos'
    dir_iframe = DIR_EXTRAS['direccionario']
    return render(request,'home/direccionario.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})

@login_required(login_url="/login/")
def stockcentral(request):
    Nombre='Stock Central'
    
    stock = StockCentral.objects.all()
    myFilter = OrderFilter(request.GET, queryset=stock)
    if request.GET:
        datos = myFilter
    else:
        datos = StockCentral.objects.filter(deposito='05')
    # stock = myFilter
    # stock = OrderFilter(request.GET, queryset=StockCentral.objects.all())

    return render(request,'appConsultasTango/StockCentral.html',{'myFilter':myFilter,'articulos':datos,'Nombre':Nombre})