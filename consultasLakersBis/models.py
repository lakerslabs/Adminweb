from email.policy import default
from django.db import models


class Direccionario(models.Model):
    nro_sucursal = models.IntegerField(db_column='NRO_SUCURSAL',primary_key=True,unique=False)  # Field name made lowercase.
    cod_client = models.CharField(db_column='COD_CLIENT', max_length=8)  # Field name made lowercase.
    desc_sucursal = models.CharField(db_column='DESC_SUCURSAL', max_length=50)  # Field name made lowercase.
    canal = models.CharField(db_column='CANAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipo_local = models.CharField(db_column='TIPO_LOCAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    grupo_empresario = models.CharField(db_column='GRUPO_EMPRESARIO', max_length=60)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=60)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=50)  # Field name made lowercase.
    tango = models.CharField(db_column='TANGO', max_length=2)  # Field name made lowercase.
    base_nombre = models.CharField(db_column='BASE_NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    conexion_dns = models.CharField(db_column='CONEXION_DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tienda = models.CharField(db_column='TIENDA', max_length=2)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    horario = models.CharField(db_column='HORARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=50)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'DIRECCIONARIO'
        ordering = ['nro_sucursal']

from django.db import models


class SucursalesLakers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nro_sucursal = models.IntegerField(db_column='NRO_SUCURSAL')  # Field name made lowercase.
    cod_client = models.CharField(db_column='COD_CLIENT', max_length=8)  # Field name made lowercase.
    desc_sucursal = models.CharField(db_column='DESC_SUCURSAL', max_length=50)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=60)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=50,)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=50)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=50)  # Field name made lowercase.
    canal = models.CharField(db_column='CANAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.BooleanField(db_column='HABILITADO', blank=True, null=True)  # Field name made lowercase.
    dashboard_bi = models.BooleanField(db_column='DASHBOARD_BI', blank=True, null=True)  # Field name made lowercase.
    tango = models.BooleanField(db_column='TANGO', blank=True, null=True)  # Field name made lowercase.
    suc_madre = models.BooleanField(db_column='SUC_MADRE', blank=True, null=True)  # Field name made lowercase.
    nro_suc_madre = models.IntegerField(db_column='NRO_SUC_MADRE', blank=True, null=True)  # Field name made lowercase.
    tipo_local = models.CharField(db_column='TIPO_LOCAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    integracion_mercadopago_madre = models.BooleanField(db_column='INTEGRACION_MERCADOPAGO_MADRE', blank=True, null=True)  # Field name made lowercase.
    integracion_mercadopago_hija = models.BooleanField(db_column='INTEGRACION_MERCADOPAGO_HIJA', blank=True, null=True)  # Field name made lowercase.
    empresa_ferreteria = models.BooleanField(db_column='EMPRESA_FERRETERIA', blank=True, null=True)  # Field name made lowercase.
    conexion_dns = models.CharField(db_column='CONEXION_DNS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usuario_dns = models.CharField(db_column='USUARIO_DNS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    clave_dns = models.CharField(db_column='CLAVE_DNS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conexion_teamviewer_madre = models.CharField(db_column='CONEXION_TEAMVIEWER_MADRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    clave_teamviewer = models.CharField(db_column='CLAVE_TEAMVIEWER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    factura_elect = models.BooleanField(db_column='FACTURA_ELECT', blank=True, null=True)  # Field name made lowercase.
    lapos_integrado = models.BooleanField(db_column='LAPOS_INTEGRADO', blank=True, null=True)  # Field name made lowercase.
    link_pedido = models.CharField(db_column='LINK_PEDIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    link_sales = models.CharField(db_column='LINK_SALES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lapos_modelo = models.CharField(db_column='LAPOS_MODELO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    version_soft_lapos = models.CharField(db_column='VERSION_SOFT_LAPOS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cable_lapos_integrado = models.CharField(db_column='CABLE_LAPOS_INTEGRADO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    n_llave_tango = models.CharField(db_column='N_LLAVE_TANGO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    llave_prueba = models.BinaryField(db_column='LLAVE_PRUEBA', blank=True, null=True)  # Field name made lowercase.
    base_nombre = models.CharField(db_column='BASE_NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    conexion_teamviewer_hija = models.CharField(db_column='CONEXION_TEAMVIEWER_HIJA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usuario_pc_madre = models.CharField(db_column='USUARIO_PC_MADRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    clave_usuario_m = models.BinaryField(db_column='CLAVE_USUARIO_M', blank=True, null=True)  # Field name made lowercase.
    cod_deposi = models.CharField(db_column='COD_DEPOSI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fecha_cierre = models.DateField(db_column='FECHA_CIERRE', blank=True, null=True)  # Field name made lowercase.
    horario = models.CharField(db_column='HORARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SUCURSALES_LAKERS'