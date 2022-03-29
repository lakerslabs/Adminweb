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

@login_required(login_url="/login/")
def direccionario(request):
    Nombre='Pedidos'
    dir_iframe = DIR_EXTRAS['direccionario']
    return render(request,'home/direccionario.html',{'dir_iframe':dir_iframe,'Nombre':Nombre})