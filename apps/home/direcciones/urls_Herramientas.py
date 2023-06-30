# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from apps.home import views

urlpatterns = [
    # Logistica
    path("Calendario/TurnoListView", views.Listar_turno, name="Herramientas"),
    path('Calendario/NuevoTurnoProveedor', views.Crear_turno, name='Herramientas'),
    path('Calendario/EditarTurnoProveedor/<int:IdTurno>', views.Editar_Turno, name='Herramientas'),
    path('Gestion_cronograma', views.Gestion_cronograma, name='Herramientas'),
    path('Gestion_guias_mayoristas',
         views.Gestion_guias_mayoristas, name='Herramientas'),
    # Abastecimiento
    path('Stock_excluido', views.Stock_excluido, name='Herramientas'),
    path('Carga_de_orden', views.Carga_de_orden, name='Herramientas'),
    path('Activar_orden', views.Activar_orden, name='Herramientas'),
    path('Desactivar_orden', views.Desactivar_orden, name='Herramientas'),
    # Comercial
    path('Ventas_sucursales', views.Ventas_sucursales, name='Herramientas'),
    path('GestionCategoriaProductos', views.Gestion_categoria_productos, name='Herramientas'),
    # Mayoristas
    path('Adm_Pedido', views.Adm_Pedido, name='Herramientas'),
    # Ecommerce
    path('Control_pedidos', views.Control_pedidos, name='Herramientas'),
    path('StockSegVtex', views.StockSegVtex, name='Herramientas'),
    # Gerencia
    path('rendircobranzas/<str:UserName>', views.rendircobranzas, name='Herramientas'),
    path('GestionarCobro/<str:UserName>', views.GestionarCobro, name='Herramientas'),
    # Administracion
    path('Controlgastos', views.Controlgastos, name='Herramientas'),
    path('Cargargastos', views.Cargargastos, name='Herramientas'),
    path('Controlcajasdiario', views.Controlcajasdiario, name='Herramientas'),

    # Administracion_CE             ***Comercio Exterior***
    path('Cargarcontenedor', views.Cargarcontenedor, name='Herramientas'),
    path('EditarContenedor', views.EditarContenedor, name='Herramientas'),


]
