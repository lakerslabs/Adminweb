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
            path('stockSupply', views.stockcentral_pivot, name='stockcentral_pivot'),
            path('stockSupplyUY', views.stockcentral_pivotUY, name='stockcentral_pivotUY'),
            path('pendiente_despacho', views.Pedidos_pendiente_despacho, name='Reportes'),
            path('MovimientosWms', views.MovimientosWms, name='MovimientosWms'),
            path('ConsultaDestino', views.ConsultaDestino, name='ConsultaDestino'),
        # Abastecimiento
            path('Auditoria_orden', views.Auditoria_orden, name='Reportes'),
            path('CategoriasDeProductos', views.CategoriasDeProductos, name='Reportes'),
            path('HRecodificaciones', views.HRecodificaciones, name='Reportes'),
            path('Eficiencia_pedidos', views.Eficiencia_pedidos, name='Reportes'),
            path('promocionesActivas', views.promocionesActivas, name='Reportes'),
        # Comercial
            path('stockSucursalesLakers', views.stockSucursalesLakers, name='Reportes'),
            path('Stock_Suc_Articulos', views.Stock_Sucursales, name='Reportes'),
            path('stockSucursalesTasky', views.stockSucursalesTasky, name='Reportes'),
            path('VentasXcanal', views.VentasXcanal, name='Reportes'),
            path('AdmEmpleados', views.AdmEmpleados, name='Reportes'),
            path('AnalisisProductos', views.AnalisisProductos, name='Reportes'),
        # Mayoristas
            path('Tracking_pedidos_mayoristas', views.Tracking_pedidos_mayoristas, name='Reportes'),
        # Ecommerce
            path('stock_ecommerce', views.stockcentral_ecommerce, name='stock_ecommerce'),
            path('Tracking_Ecommerce', views.Tracking_Ecommerce, name='stock_ecommerce'),
            path('stockUY_ecommerce', views.stockUY_ecommerce, name='stockUY_ecommerce'),
            path('Pedidos', views.Pedidos, name='Reportes'),
            path('PedidosUY', views.PedidosUY, name='Reportes'),
            path('Auditoria_Ecommerce', views.Auditoria_Ecommerce, name='Reportes'),
            path('Auditoria_Prisma', views.Auditoria_Prisma, name='Reportes'),
            path('Segmentacion_clientes', views.Segmentacion_clientes, name='Reportes'),
            path('TableroDeControl', views.TableroDeControl, name='Reportes'),
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
            path('FacturaManualLista', views.facturas_por_fecha, name='Reportes'),
            path('ContratosFranquicias', views.ContratosFranquicias, name='Reportes'),
]