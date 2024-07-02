# -*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.core.validators import RegexValidator


class StockCentral(models.Model):
    articulo = models.CharField(db_column='COD_ARTICU', max_length=15,primary_key=True,unique=False)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deposito = models.CharField(db_column='COD_DEPOSI', max_length=2)  # Field name made lowercase.
    total = models.FloatField(db_column='STOCK_TOTAL', blank=True, null=True)  # Field name made lowercase.
    comp = models.FloatField(db_column='CANT_COMP', blank=True, null=True)  # Field name made lowercase.
    reserva = models.IntegerField(db_column='CANT_RESERVA')  # Field name made lowercase.
    excluido = models.IntegerField(db_column='STOCK_EXCLUIDO')  # Field name made lowercase.
    disponible = models.FloatField(db_column='STOCK_DISPONIBLE')  # Field name made lowercase.
    destino = models.CharField(db_column='DESTINO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='RUBRO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temporada = models.CharField(db_column='TEMPORADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'STOCK_CENTRAL'


    def __str__(self):
        return self.articulo

class SjStockDisponibleEcommerce(models.Model):
    articulo = models.CharField(db_column='COD_ARTICU', max_length=15,primary_key=True,unique=False)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deposito = models.CharField(db_column='COD_DEPOSI', max_length=2)  # Field name made lowercase.
    total = models.FloatField(db_column='STOCK', blank=True, null=True)  # Field name made lowercase.
    stock_seguridad = models.FloatField(db_column='STOCK_SEGURIDAD', blank=True, null=True)  # Field name made lowercase.
    cant_comp = models.FloatField(db_column='CANT_COMP', blank=True, null=True)  # Field name made lowercase.
    reserva_ecommerce = models.FloatField(db_column='RESERVA_ECOMMERCE', blank=True, null=True)  # Field name made lowercase.
    stock_reserva_vtex = models.FloatField(db_column='STOCK_RESERVA_VTEX', blank=True, null=True)  # Field name made lowercase.
    stock_excluido = models.FloatField(db_column='STOCK_EXCLUIDO', blank=True, null=True)  # Field name made lowercase.
    stock_disponible = models.FloatField(db_column='STOCK_DISPONIBLE', blank=True, null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='RUBRO', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'SJ_STOCK_DISPONIBLE_ECOMMERCE'

class Turno(models.Model):
    IdTurno = models.AutoField(primary_key=True)
    CodigoProveedor = models.CharField(max_length=6,null=False, blank=False)
    FechaAsignacion = models.DateTimeField()
    OrdenCompra = models.CharField(max_length=14,null=False, blank=False)
    Remitos = models.CharField(max_length=100,null=False, blank=False)
    CantidadUnidades = models.IntegerField(null=False, blank=False)
    CantidadBultos = models.IntegerField(null=True, blank=True)
    Recepcionado = models.BooleanField(default=False)
    Auditado = models.BooleanField(default=False)
    Posicionado = models.BooleanField(default=False)
    Observaciones = models.CharField(max_length=300, null=True, blank=True)
    CodigoError = models.IntegerField(null=True, blank=True)
    RecepcionadoFechaHora = models.DateTimeField(null=True, blank=True)
    AuditadoFechaHora = models.DateTimeField(null=True, blank=True)
    PosicionadoFechaHora = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.IdTurno} - {self.OrdenCompra}'

class CodigosError(models.Model):
    CodigoError = models.IntegerField(primary_key=True)
    DescripcionError = models.CharField(max_length=100)

class EB_facturaManual(models.Model):
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    numeroSucursal = models.IntegerField()
    tipoFactura = models.IntegerField(choices=[(0, 'Factura-A'), (1, 'Factura-B')])
    numeroFactura = models.CharField(max_length=14, validators=[RegexValidator(regex='^\d{5}-\d{8}$', message='El formato debe ser XXXXX-XXXXXXX')])
    imgFactura = models.ImageField(upload_to='images/', blank=True, null=True)