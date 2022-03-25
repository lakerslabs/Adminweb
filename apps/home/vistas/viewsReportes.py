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
from apps.home.vistas.settingsUrls import *

# Logistica

@login_required(login_url="/login/")
def Pedidos_pendiente_despacho(request):
    Nombre='Pedidos_pendiente_despacho'
    dir_iframe = DIR_REPORTES['Pedidos_pendiente_despacho']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})

# Abastecimiento

@login_required(login_url="/login/")
def Auditoría_orden(request):
    Nombre='Auditoría_orden'
    dir_iframe = DIR_REPORTES['Auditoría_orden']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})


# Comercial

@login_required(login_url="/login/")
def Stock_Sucursales(request):
    Nombre='Stock_Sucursales'
    dir_iframe = DIR_REPORTES['Stock_Sucursales']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})

@login_required(login_url="/login/")
def Stock_central(request):
    Nombre='Stock_central'
    dir_iframe = DIR_REPORTES['Stock_central']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})


# Mayoristas

@login_required(login_url="/login/")
def Tracking_pedidos_mayoristas(request):
    Nombre='Tracking_pedidos_mayoristas'
    dir_iframe = DIR_REPORTES['Tracking_pedidos_mayoristas']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})


# Ecommerce

@login_required(login_url="/login/")
def Pedidos(request):
    Nombre='Pedidos'
    dir_iframe = DIR_REPORTES['Pedidos']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})

@login_required(login_url="/login/")
def Auditoría_Ecommerce(request):
    Nombre='Auditoría_Ecommerce'
    dir_iframe = DIR_REPORTES['Auditoría_Ecommerce']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})

@login_required(login_url="/login/")
def Auditoría_Prisma(request):
    Nombre='Auditoría_Prisma'
    dir_iframe = DIR_REPORTES['Auditoría_Prisma']
    return render(request,'home/PlantillaReportes.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})