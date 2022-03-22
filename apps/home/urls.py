# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # The transporte page
    path('transporte', views.transporte, name='transporte'),
    path('direccionario', views.direccionario, name='direccionario'),
    path('salesucursales', views.sale_sucursales, name='direccionario'),
    path('transporte/crearTransporte', views.crearTransporte, name='crearTransporte'),
    path('eliminarTransporte/<int:id>', views.eliminarTransporte, name='eliminarTransporte'),
    path('transporte/editarTransporte/<int:id>', views.editarTransporte, name='editarTransporte'),

    path('reservarsala', views.reservar, name='reserva'),
    path('reservarsala2', views.reservarTurnos, name='reserva'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

    
]
