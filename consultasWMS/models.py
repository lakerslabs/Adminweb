# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RoMovimientosWms(models.Model):
    nro_tarea = models.IntegerField(db_column='NRO_TAREA', blank=True, null=True)  # Field name made lowercase.
    nro_movim = models.IntegerField(db_column='NRO_MOVIM',primary_key=True,unique=False)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod_articulo = models.CharField(db_column='COD_ARTICULO', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    tipo_movimiento = models.CharField(db_column='TIPO_MOVIMIENTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ubic_origen = models.CharField(db_column='UBIC_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    depo_origen = models.CharField(db_column='DEPO_ORIGEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ubic_destino = models.CharField(db_column='UBIC_DESTINO', max_length=10)  # Field name made lowercase.
    depo_destino = models.CharField(db_column='DEPO_DESTINO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'RO_MOVIMIENTOS_WMS'
