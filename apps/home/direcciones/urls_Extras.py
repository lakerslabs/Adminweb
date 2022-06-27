# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Extras"
urlpatterns = [
            path('importFileUbi', views.import_file_ubi, name='uploadFile'),
            path('importfilecierrePedidos', views.import_file_cierrePedidos, name='uploadFilecierrePedidos'),
        # Logistica
        # Abastecimiento
        # Comercial
            path('direccionario', views.direccionario, name='Extras'),
        # Mayoristas
        # Ecommerce
        # Gerencia

]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)