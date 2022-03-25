# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.direcciones import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # The transporte page
    path('transporte', views.transporte, name='transporte'),
    path('transporte/crearTransporte', views.crearTransporte, name='crearTransporte'),
    path('eliminarTransporte/<int:id>', views.eliminarTransporte, name='eliminarTransporte'),
    path('transporte/editarTransporte/<int:id>', views.editarTransporte, name='editarTransporte'),

    path('reservarsala', views.reservar, name='reserva'),
    path('reservarsala2', views.reservarTurnos, name='reserva'),


    # Logistica
    path('Kpis_Logistica', views.Kpis_Logistica, name='Dashboard_PowerBI'), 
    path('Pedidos_pendiente_despacho', views.Pedidos_pendiente_despacho, name='Reportes'),

    # Abastecimiento
    path('Auditoría_orden', views.Auditoría_orden, name='Reportes'),


    # Comercial
    path('Promociones', views.Promociones, name='Dashboard_PowerBI'),
    path('Inventarios_Sucursales', views.Inventarios_Sucursales, name='Dashboard_PowerBI'),
    path('Conteos', views.Conteos, name='Dashboard_PowerBI'),
    path('Geodatos', views.Geodatos, name='Dashboard_PowerBI'),
    path('Notas_de_credito', views.Notas_de_credito, name='Dashboard_PowerBI'),
    path('Ventas_Franquicias', views.Ventas_Franquicias, name='Dashboard_PowerBI'),
    path('Ventas_Sucursales', views.Ventas_Sucursales, name='Dashboard_PowerBI'),
    path('Velocidad_de_Ventas', views.Velocidad_de_Ventas, name='Dashboard_PowerBI'),
    path('Stock_Sucursales', views.Stock_Sucursales, name='Reportes'),
    path('Stock_central', views.Stock_central, name='Reportes'),
    

    # Mayoristas
    path('Ventas_Mayoristas', views.Ventas_Mayoristas, name='Dashboard_PowerBI'),
    path('Tracking_pedidos_mayoristas', views.Tracking_pedidos_mayoristas, name='Reportes'),


    # Ecommerce
    path('Ventas_Ecommerce', views.Ventas_Ecommerce, name='Dashboard_PowerBI'),
    path('Kpis_Ecommerce', views.Kpis_Ecommerce, name='Dashboard_PowerBI'),
    path('Pedidos', views.Pedidos, name='Reportes'),
    path('Auditoría_Ecommerce', views.Auditoría_Ecommerce, name='Reportes'),
    path('Auditoría_Prisma', views.Auditoría_Prisma, name='Reportes'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

    
]
