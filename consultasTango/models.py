# -*- encoding:utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models


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
        db_table = 'STOCK_CENTRAL_EDU'


    def __str__(self):
        return self.articulo