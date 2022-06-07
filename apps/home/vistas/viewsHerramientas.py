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

# @login_required(login_url="/login/")
# def (request):
#     Nombre=''
#     dir_iframe = DIR_REPORTES['']
#     return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})


# Logistica
@login_required(login_url="/login/")
def Gestion_cronograma(request):
    Nombre='Gestión cronograma'
    dir_iframe = DIR_HERAMIENTAS['Gestion_cronograma']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

@login_required(login_url="/login/")
def Gestion_guias_mayoristas(request):
    Nombre='Guías mayoristas'
    dir_iframe = DIR_HERAMIENTAS['Gestion_guias_mayoristas']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

# Abastecimiento
@login_required(login_url="/login/")
def Stock_excluido(request):
    Nombre='Stock excluido'
    dir_iframe = DIR_HERAMIENTAS['Stock_excluido']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

@login_required(login_url="/login/")
def Carga_de_orden(request):
    Nombre='Carga de orden'
    dir_iframe = DIR_HERAMIENTAS['Carga_de_orden']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

@login_required(login_url="/login/")
def Activar_orden(request):
    Nombre='Activar orden'
    dir_iframe = DIR_HERAMIENTAS['Activar_orden']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

@login_required(login_url="/login/")
def Desactivar_orden(request):
    Nombre='Desactivar orden'
    dir_iframe = DIR_HERAMIENTAS['Desactivar_orden']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

# Comercial
@login_required(login_url="/login/")
def Ventas_sucursales(request):
    Nombre='Ventas sucursales'
    dir_iframe = DIR_HERAMIENTAS['Ventas_sucursales']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

# Mayoristas
@login_required(login_url="/login/")
def Adm_Pedido(request):
    Nombre='Adm Pedido'
    dir_iframe = DIR_HERAMIENTAS['Adm_Pedido']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})

# Ecommerce
@login_required(login_url="/login/")
def Control_pedidos(request):
    Nombre='Control pedidos'
    dir_iframe = DIR_HERAMIENTAS['Control_pedidos']
    return render(request,'home/PlantillaHerramientas.html',{'dir_iframe':dir_iframe,})
