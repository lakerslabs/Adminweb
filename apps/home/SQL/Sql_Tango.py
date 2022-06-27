from django.db import connections

def validar_pedido(pedido,talon_pedido):
    with connections['mi_db_2'].cursor() as cursor:
        
        sql = '''SELECT COUNT(*) CONTAR FROM 
                    (
                    SELECT * FROM GVA21 WHERE TALON_PED = '''+ "'" + talon_pedido + "'"''' AND NRO_PEDIDO = '''+ "'" + pedido + "'"''' AND ESTADO = 2) A
                    '''
        cursor.execute(sql)
        # print(sql)
        resulatado = cursor.fetchone()
        # print(resulatado[0])
    return int(resulatado[0])

def cerrar_pedido(talon_pedido,pedido):
    with connections['mi_db_2'].cursor() as cursor:
        sql = '''EXEC RO_ANULAR_PEDIDOS ''' + talon_pedido + ",'" + pedido + "'"
        # print(sql)
        cursor.execute(sql) # Guarda los cambios en la base de datos