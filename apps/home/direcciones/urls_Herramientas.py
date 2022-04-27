# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
        # Logistica
            path('Gestion_cronograma', views.Gestion_cronograma, name='Herramientas'),
            path('Gestion_guias_mayoristas', views.Gestion_guias_mayoristas, name='Herramientas'),
        # Abastecimiento
            path('Carga_de_orden', views.Carga_de_orden, name='Herramientas'),
            path('Activar_orden', views.Activar_orden, name='Herramientas'),
            path('Desactivar_orden', views.Desactivar_orden, name='Herramientas'),
        # Comercial
            path('Ventas_sucursales', views.Ventas_sucursales, name='Herramientas'),
        # Mayoristas
        # Ecommerce
            path('Control_pedidos', views.Control_pedidos, name='Herramientas'),
        # Gerencia
]