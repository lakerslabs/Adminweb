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
    path('transporte/crearTransporte', views.crearTransporte, name='crearTransporte'),
    path('eliminarTransporte/<int:id>', views.eliminarTransporte, name='eliminarTransporte'),
    path('transporte/editarTransporte/<int:id>', views.editarTransporte, name='editarTransporte'),

    path('reservarsala', views.reservar, name='reserva'),
    path('reservarsala2', views.reservarTurnos, name='reserva'),


    # Logistica
    path('Kpis_Logistica', views.Kpis_Logistica, name='Dashboard_PowerBI'), 
    path('Pedidos_pendiente_despacho', views.Pedidos_pendiente_despacho, name='Reportes'),
    path('Gestion_cronograma', views.Gestion_cronograma, name='Herramientas'),
    path('Gestion_guias_mayoristas', views.Gestion_guias_mayoristas, name='Herramientas'),
    

    # Abastecimiento
    path('Auditoria_orden', views.Auditoria_orden, name='Reportes'),
    path('Carga_de_orden', views.Carga_de_orden, name='Herramientas'),
    path('Activar_orden', views.Activar_orden, name='Herramientas'),
    path('Desactivar_orden', views.Desactivar_orden, name='Herramientas'),


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
    path('Ventas_sucursales', views.Ventas_sucursales, name='Herramientas'),
    

    # Mayoristas
    path('Ventas_Mayoristas', views.Ventas_Mayoristas, name='Dashboard_PowerBI'),
    path('Tracking_pedidos_mayoristas', views.Tracking_pedidos_mayoristas, name='Reportes'),


    # Ecommerce
    path('Ventas_Ecommerce', views.Ventas_Ecommerce, name='Dashboard_PowerBI'),
    path('Kpis_Ecommerce', views.Kpis_Ecommerce, name='Dashboard_PowerBI'),
    path('Pedidos', views.Pedidos, name='Reportes'),
    path('Auditoria_Ecommerce', views.Auditoria_Ecommerce, name='Reportes'),
    path('Auditoria_Prisma', views.Auditoria_Prisma, name='Reportes'),
    path('Control_pedidos', views.Control_pedidos, name='Herramientas'),

    # Extras
    path('direccionario', views.direccionario, name='Extras'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    

    
]
