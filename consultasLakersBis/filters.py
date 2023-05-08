import django_filters
from consultasLakersBis.models import SofStockLakers
from django.db import connections

# Consultas sql para traer los items de los filtros 
def filtroCanal():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select CANAL from DIRECCIONARIO
                        group by CANAL
                        ''')
        consulta = cursor.fetchall()

        lista=[]
        for c in consulta:
            lista.append(c[0])
    return lista

def filtroTipoLocal():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select TIPO_LOCAL from DIRECCIONARIO
                        group by TIPO_LOCAL
                        ''')
        consulta = cursor.fetchall()

        lista=[]
        for c in consulta:
            lista.append(c[0])
    return lista

def filtroGrupoEmpresario():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select GRUPO_EMPRESARIO from DIRECCIONARIO
                        where GRUPO_EMPRESARIO != ''
                        group by GRUPO_EMPRESARIO
                        order by GRUPO_EMPRESARIO
                        ''')
        consulta = cursor.fetchall()

        lista=[]
        for c in consulta:
            lista.append(c[0])
    return lista

def filtroRubro():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(RUBRO,'SIN RUBRO')RUBRO from SOF_STOCK_LAKERS
                        group by RUBRO
                        order by RUBRO
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroTemporada():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(TEMPORADA,'SIN TEMPORADA')TEMPORADA from SOF_STOCK_LAKERS
                        group by TEMPORADA
                        order by TEMPORADA
                        ''')
        row = list(cursor.fetchall())
    return row

def filtroDescSuc():
    with connections['mi_db_4'].cursor() as cursor:
        cursor.execute('''
                        select  ISNULL(DESC_SUCURSAL,'SIN')DESC_SUCURSAL from SOF_STOCK_LAKERS
                        group by DESC_SUCURSAL
                        order by DESC_SUCURSAL
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

# Clase para aplicar filtros a la consulta de stock
class SucFilter(django_filters.FilterSet):
    # Cargar los items de los filtros en la variable Deposito
    consulta = filtroDescSuc()
    SUCURSAL = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Temporada
    consulta = filtroTemporada()
    TEMPORADA = itemsFiltros(consulta)
    # Cargar los items de los filtros en la variable Rubro
    consulta = filtroRubro()
    RUBRO = itemsFiltros(consulta)
    
    class Meta:
        model = SofStockLakers
        fields = ['desc_sucursal','temporada','rubro']   
    
    desc_sucursal = django_filters.ChoiceFilter(label='SUCURSAL ', choices=SUCURSAL)
    temporada = django_filters.ChoiceFilter(label='TEMPORADA ', choices=TEMPORADA)
    rubro = django_filters.ChoiceFilter(label='RUBRO ', choices=RUBRO)