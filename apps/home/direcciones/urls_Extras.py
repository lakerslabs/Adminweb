# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views


urlpatterns = [
        # Logistica
        # Abastecimiento
        # Comercial
            path('direccionario', views.direccionario, name='Extras'),
        # Mayoristas
        # Ecommerce
        # Gerencia

]