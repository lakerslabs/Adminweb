# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views


urlpatterns = [
        # RRHH
            path('AsistenciasSuc', views.AsistenciasSuc, name='AsistenciasSuc'),
        # Logistica
            path('stockcentral', views.stockcentral, name='stockcentral'),
            path('stockcUY', views.stockcUY, name='stockcUY'),
            path('pendiente_despacho', views.Pedidos_pendiente_despacho, name='Reportes'),
            path('MovimientosWms', views.MovimientosWms, name='MovimientosWms'),
        # Abastecimiento
            path('Auditoria_orden', views.Auditoria_orden, name='Reportes'),
            path('CategoriasDeProductos', views.CategoriasDeProductos, name='Reportes'),
            path('HRecodificaciones', views.HRecodificaciones, name='Reportes'),
        # Comercial
            path('Stock_Suc_Articulos', views.stockLakers, name='Reportes'),
            path('Stock_Sucursales', views.Stock_Sucursales, name='Reportes'),
            # path('Stock_central', views.Stock_central, name='Reportes'),  #Borrar este path
        # Mayoristas
            path('Tracking_pedidos_mayoristas', views.Tracking_pedidos_mayoristas, name='Reportes'),
        # Ecommerce
            path('stock_ecommerce', views.stockcentral_ecommerce, name='stock_ecommerce'),
            path('stockUY_ecommerce', views.stockUY_ecommerce, name='stockUY_ecommerce'),
            path('Pedidos', views.Pedidos, name='Reportes'),
            path('PedidosUY', views.PedidosUY, name='Reportes'),
            path('Auditoria_Ecommerce', views.Auditoria_Ecommerce, name='Reportes'),
            path('Auditoria_Prisma', views.Auditoria_Prisma, name='Reportes'),
            path('Segmentación_clientes', views.Segmentación_clientes, name='Reportes'),
        # Gerencia
            path('DetalleRemitos599/<str:UserName>', views.DetalleRemitos599, name='Reportes'),
            path('ChequesRecibidos/<str:UserName>', views.ChequesRecibidos, name='Reportes'),
        # Administracion
            path('VentasXmedio_pago', views.VentasXmedio_pago, name='Reportes'),
            path('Consultagastos', views.Consultagastos, name='Reportes'),
            path('VentaVscobranza', views.VentaVscobranza, name='Reportes'),
            path('Controlcajasmensual', views.Controlcajasmensual, name='Reportes'),
            path('ResumenMensualAlquileres', views.ResumenMensualAlquileres, name='Reportes'),
            path('CargaGastosTesoreria', views.CargaGastosTesoreria, name='Reportes'),
            path('DetalleContratosDeAlquiler', views.DetalleContratosDeAlquiler, name='Reportes'),
]