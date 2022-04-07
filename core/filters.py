from cProfile import label
from pyexpat import model
import django_filters

from consultasTango.models import *
from django.db import connections

# Consultas sql para traer los items de los filtros 
def filtroTemporada():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(TEMPORADA,'SIN')TEMPORADA from STOCK_CENTRAL
                        group by TEMPORADA
                        order by TEMPORADA desc
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroDeposito():
    with connections['mi_db_2'].cursor() as cursor:
        cursor.execute('''
                        select  COD_DEPOSI from STOCK_CENTRAL
                        group by COD_DEPOSI
                        order by COD_DEPOSI
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

# Cargar los items de los filtros en la variable Temporada
consulta = filtroTemporada()
TEMPORADA = itemsFiltros(consulta)
# Cargar los items de los filtros en la variable Deposito
consulta = filtroDeposito()
DEPOSITO = itemsFiltros(consulta)

# Clase para aplicar filtros a la consulta
class OrderFilter(django_filters.FilterSet):
    
    class Meta:
        model = StockCentral
        # fields = {
        #     'deposito': ['icontains'],
        # }
        exclude = ['articulo','descripcion','deposito','total','comp','reserva','excluido','disponible','destino','rubro','categoria','temporada','color']

    deposito = django_filters.ChoiceFilter(label='Deposito', choices=DEPOSITO)
    temporada = django_filters.ChoiceFilter(label='Temporada', choices=TEMPORADA)




# print(consulta)