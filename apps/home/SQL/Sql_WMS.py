from django.db import connections
from numpy import isnan

# Valida ubicacion y devuelve @idUbicacion si es correcto
def validar_ubicacion(ubicacion):
    with connections['mi_db_3'].cursor() as cursor:
        sql = '''
            IF(select COUNT(id_Ubicacion) from Ubicacion where Cod_Ubicacion = '''+ "'" + ubicacion + "'"''')>0
	            select id_Ubicacion as Ubicacion from Ubicacion where Cod_Ubicacion = '''+ "'" + ubicacion + "'"'''
            ELSE
	            select COUNT(id_Ubicacion) as Ubicacion from Ubicacion where Cod_Ubicacion = '''+ "'" + ubicacion + "'"
        cursor.execute(sql)
        resulatado = cursor.fetchone()
    return int(resulatado[0])

def actualizar_ubicacion(Id_ubicacion,nombre_ubicacion,tipo_ubicacion,estado_u,rack,modulo,altura):
    instruccion = 'update Ubicacion set '
    datos = ''
    condicion = ' where id_Ubicacion='+ "'" + Id_ubicacion + "'"
    if  len(nombre_ubicacion)>0:
        datos = datos + 'Nombre_Ubicacion=' + "'" + nombre_ubicacion + "'"
    if  len(tipo_ubicacion)>0:
        datos = datos + ',Tipo_Ubicacion=' + "'" + tipo_ubicacion + "'"
    if  len(estado_u)>0:
        datos = datos + ',Estado_U=' + "'" + estado_u + "'"
    if  not isnan(rack) or rack !='':
        datos = datos + ',Rack=' + "'" + str(rack) + "'"
    if  not isnan(modulo) or modulo !='':
        datos = datos + ',Modulo=' + "'" + str(modulo) + "'"
    if  not isnan(altura) or altura !='':
        datos = datos + ',Altura=' + "'" + str(altura) + "'"
    
    sql = instruccion + datos + condicion
    print(sql)
    # La instruccion siguiente actuañiza los valores en la base de datos
    # with connections['mi_db_3'].cursor() as cursor:
    #     cursor.execute(sql)
    #     # resulatado = cursor.fetchone()
    return 