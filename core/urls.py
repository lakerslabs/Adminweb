# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),             # UI Kits Html files
    path("Dashboard/", include("apps.home.direcciones.urls_Dashboard")),
    path("Reportes/", include("apps.home.direcciones.urls_Reportes")),
    path("Herramientas/", include("apps.home.direcciones.urls_Herramientas")),
    path("Extras/", include("apps.home.direcciones.urls_Extras")),
]
