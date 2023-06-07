# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views


urlpatterns = [
        # Logistica
            path('stockcentral', views.stockcentral, name='stockcentral'),
            path('pendiente_despacho', views.Pedidos_pendiente_despacho, name='Reportes'),
            path('MovimientosWms', views.MovimientosWms, name='MovimientosWms'),
        # Abastecimiento
            path('Auditoria_orden', views.Auditoria_orden, name='Reportes'),
        # Comercial
            path('Stock_Suc_Articulos', views.stockLakers, name='Reportes'),
            path('Stock_Sucursales', views.Stock_Sucursales, name='Reportes'),
            # path('Stock_central', views.Stock_central, name='Reportes'),  #Borrar este path
        # Mayoristas
            path('Tracking_pedidos_mayoristas', views.Tracking_pedidos_mayoristas, name='Reportes'),
        # Ecommerce
            path('stock_ecommerce', views.stockcentral_ecommerce, name='stock_ecommerce'),
            path('Pedidos', views.Pedidos, name='Reportes'),
            path('Auditoria_Ecommerce', views.Auditoria_Ecommerce, name='Reportes'),
            path('Auditoria_Prisma', views.Auditoria_Prisma, name='Reportes'),
        # Gerencia
            path('DetalleRemitos599', views.DetalleRemitos599, name='Reportes'),
            path('ChequesRecibidos', views.ChequesRecibidos, name='Reportes'),
        # Administracion
            path('VentasXmedio_pago', views.VentasXmedio_pago, name='Reportes'),
            path('Consultagastos', views.Consultagastos, name='Reportes'),
            path('VentaVscobranza', views.VentaVscobranza, name='Reportes'),
            path('Controlcajasmensual', views.Controlcajasmensual, name='Reportes'),
]