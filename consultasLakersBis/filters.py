# import django_filters

# from consultasLakersBis.models import Direccionario
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