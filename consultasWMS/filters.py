from cProfile import label
from pyexpat import model
import django_filters
from django_filters import DateFilter

from consultasWMS.models import *
from django.db import connections
from django.forms.widgets import DateInput

# Consultas sql para traer los items de los filtros 
def filtroUsuario():
    with connections['mi_db_3'].cursor() as cursor:
        cursor.execute('''
                        SELECT [UserName]
                        FROM [UbicacionesStockMvc].[dbo].[AspNetUsers]
                        where [LockoutEnabled]!=1
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroDeposito():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  COD_SUCURS from STA22
                        where INHABILITA = 0
                        AND COD_SUCURS != 'FA'
                        and ABASTECE = 0
                        group by COD_SUCURS
                        order by COD_SUCURS
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroMovimientos():
    with connections['mi_db_3'].cursor() as cursor:
        cursor.execute('''
                        select TIPO_MOVIMIENTO from RO_MOVIMIENTOS_WMS
                        where TIPO_MOVIMIENTO != 'NULL'
                        GROUP BY TIPO_MOVIMIENTO
                        ''')
        row = list(cursor.fetchall())
    return row

# Funcion que arma una tupla con los parametros de filtros
def itemsFiltros(consulta):
    lista=[]
    for c in consulta:
        lista.append(tuple([c[0],c[0].lower()]))
        opciones=tuple(lista)   
    return opciones


# Clase para aplicar filtros a la consulta de stock central
class OrderFilter(django_filters.FilterSet):
    # Cargar los items de los filtros en la variable Deposito
    consulta = filtroDeposito()
    DEPOSITO = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Temporada
    consulta = filtroUsuario()
    USER = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Rubro
    consulta = filtroMovimientos()
    MOVIMIENTOS = itemsFiltros(consulta)
    

    class Meta:
        model = RoMovimientosWms
        # fields = {
        #     'nro_tarea': ['icontains'],
        # }
        exclude = ['nro_tarea','nro_movim','fecha','hora','cod_articulo','descripcion','cantidad','tipo_movimiento','ubic_origen','depo_origen','ubic_destino','depo_destino','usuario']

    nro_tarea=django_filters.CharFilter(field_name='nro_tarea', label='TAREA N° ', lookup_expr='icontains')
    fecha_desde = DateFilter(field_name='fecha', lookup_expr='gte',label='DESDE ', widget=DateInput(attrs={'type': 'date'}))
    fecha_hasta = DateFilter(field_name='fecha', lookup_expr='lte',label='HASTA ', widget=DateInput(attrs={'type': 'date'}))
    usuario = django_filters.ChoiceFilter(label='USUARIO ', choices=USER)
    depo_destino = django_filters.ChoiceFilter(label='DEPOSITO ', choices=DEPOSITO)
    tipo_movimiento = django_filters.ChoiceFilter(label='TIPO DE MOVIMIENTO ', choices=MOVIMIENTOS)
    cod_articulo = django_filters.CharFilter(field_name='cod_articulo', label='CODIGO DE ARTICULO ', lookup_expr='icontains')

# # Clase para aplicar filtros a la consulta de stock central ecommerce
# class filtro_stock_ecommerce(django_filters.FilterSet):
#     # Cargar los items de los filtros en la variable Deposito
#     consulta = filtroDeposito()
#     DEPOSITO = itemsFiltros(consulta)
#     # Cargar los items de los filtros en la variable Rubro
#     consulta = filtroRubro()
#     RUBRO = itemsFiltros(consulta)
    
#     class Meta:
#         model = RoMovimientosWms
#         # fields = [...]
#         exclude = ['articulo','descripcion','deposito','total','stock_seguridad','cant_comp','reserva_ecommerce','stock_reserva_vtex','stock_excluido','stock_disponible','rubro']

#     # deposito = django_filters.ChoiceFilter(label='DEPOSITO ', choices=DEPOSITO)
#     rubro = django_filters.ChoiceFilter(label='RUBRO ', choices=RUBRO)
