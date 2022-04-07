# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StockCentral(models.Model):
    cod_articu = models.CharField(db_column='COD_ARTICU', max_length=15)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_deposi = models.CharField(db_column='COD_DEPOSI', max_length=2)  # Field name made lowercase.
    stock_total = models.FloatField(db_column='STOCK_TOTAL', blank=True, null=True)  # Field name made lowercase.
    cant_comp = models.FloatField(db_column='CANT_COMP', blank=True, null=True)  # Field name made lowercase.
    cant_reserva = models.IntegerField(db_column='CANT_RESERVA')  # Field name made lowercase.
    stock_excluido = models.IntegerField(db_column='STOCK_EXCLUIDO')  # Field name made lowercase.
    stock_disponible = models.FloatField(db_column='STOCK_DISPONIBLE')  # Field name made lowercase.
    destino = models.CharField(db_column='DESTINO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='RUBRO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='CATEGORIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temporada = models.CharField(db_column='TEMPORADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'STOCK_CENTRAL'
