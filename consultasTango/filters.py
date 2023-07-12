from cProfile import label
from pyexpat import model
import django_filters

from consultasTango.models import *
from django.db import connections

# Consultas sql para traer los items de los filtros 
def filtroTemporada():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(TEMPORADA,'SIN')TEMPORADA from SOF_MAESTRO_ARTICULOS_RUBRO_CATEGORIA
                        group by TEMPORADA
                        order by TEMPORADA desc
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroDeposito():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  COD_SUCURS from STA22
						where INHABILITA = 0
						AND COD_SUCURS IN ('01','02','03','04','05','06','07','08','09','10','11','12','20')
                        group by COD_SUCURS
                        order by COD_SUCURS
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroRubro():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(RUBRO,'SIN')RUBRO from SOF_MAESTRO_ARTICULOS_RUBRO_CATEGORIA
                        group by RUBRO
                        order by RUBRO desc
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
    consulta = filtroTemporada()
    TEMPORADA = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Rubro
    consulta = filtroRubro()
    RUBRO = itemsFiltros(consulta)
    
    class Meta:
        model = StockCentral
        # fields = {
        #     'deposito': ['icontains'],
        # }
        exclude = ['articulo','descripcion','deposito','total','comp','reserva','excluido','disponible','destino','rubro','categoria','temporada','color']

    deposito = django_filters.ChoiceFilter(label='DEPOSITO ', choices=DEPOSITO)
    temporada = django_filters.ChoiceFilter(label='TEMPORADA ', choices=TEMPORADA)
    rubro = django_filters.ChoiceFilter(label='RUBRO ', choices=RUBRO)

# Clase para aplicar filtros a la consulta de stock central ecommerce
class filtro_stock_ecommerce(django_filters.FilterSet):
    # Cargar los items de los filtros en la variable Deposito
    consulta = filtroDeposito()
    DEPOSITO = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Rubro
    consulta = filtroRubro()
    RUBRO = itemsFiltros(consulta)
    
    class Meta:
        model = SjStockDisponibleEcommerce
        # fields = [...]
        exclude = ['articulo','descripcion','deposito','total','stock_seguridad','cant_comp','reserva_ecommerce','stock_reserva_vtex','stock_excluido','stock_disponible','rubro']

    # deposito = django_filters.ChoiceFilter(label='DEPOSITO ', choices=DEPOSITO)
    rubro = django_filters.ChoiceFilter(label='RUBRO ', choices=RUBRO)
