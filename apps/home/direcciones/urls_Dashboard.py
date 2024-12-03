# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
        # Logistica
        path('Kpis_Logistica', views.Kpis_Logistica, name='Dashboard_PowerBI'),
        # Abastecimiento
        # Comercial
            path('Promociones', views.Promociones, name='Dashboard_PowerBI'),
            path('Inventarios_Sucursales', views.Inventarios_Sucursales, name='Dashboard_PowerBI'),
            path('Conteos', views.Conteos, name='Dashboard_PowerBI'),
            path('Geodatos', views.Geodatos, name='Dashboard_PowerBI'),
            path('Notas_de_credito', views.Notas_de_credito, name='Dashboard_PowerBI'),
            path('Ventas_Franquicias', views.Ventas_Franquicias, name='Dashboard_PowerBI'),
            path('Ventas_Sucursales', views.Ventas_Sucursales, name='Dashboard_PowerBI'),
            path('Ventas_SucursalesUY', views.Ventas_SucursalesUY, name='Dashboard_PowerBI'),
            path('Velocidad_de_Ventas', views.Velocidad_de_Ventas, name='Dashboard_PowerBI'),
        # Mayoristas
            path('Ventas_Mayoristas', views.Ventas_Mayoristas, name='Dashboard_PowerBI'),
        # Ecommerce
            path('Ventas_Ecommerce', views.Ventas_Ecommerce, name='Dashboard_PowerBI'),
            path('Kpis_Ecommerce', views.Kpis_Ecommerce, name='Dashboard_PowerBI'),
            path('PromocionesEcommerce', views.PromocionesEcommerce, name='Dashboard_PowerBI'),
        # Gerencia
            path('PremiosComercial', views.PremiosComercial, name='Dashboard_PowerBI'),
]
