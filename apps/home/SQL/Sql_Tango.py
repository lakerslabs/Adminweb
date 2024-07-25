from django.db import connections

def validar_articulo(articulo):
    with connections['mi_db_2'].cursor() as cursor:
        
        sql = '''SELECT COUNT(*) CONTAR FROM 
                    (
                    SELECT * FROM SJ_ETIQUETAS_FINAL WHERE COD_ARTICU = '''+ "'" + articulo + "'"''') A
                    '''
        cursor.execute(sql)
        # print(sql)
        resulatado = cursor.fetchone()
        # print(resulatado[0])
    return int(resulatado[0])

def cargar_articulo(articulo, descripcion):
    with connections['mi_db_2'].cursor() as cursor:
        sql = '''INSERT INTO SJ_T_ETIQUETAS_FINAL (COD_ARTICU, DESCRIPCIO) VALUES (''' + "'" + articulo + "'" + ',' + "'" + descripcion + "'" + ')'
        cursor.execute(sql)

def borrar_contTabla(nombre_tabla):
    with connections['mi_db_2'].cursor() as cursor:        
        sql = '''DELETE FROM '''+ nombre_tabla
        cursor.execute(sql)

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

def validar_pedidoAsignado(pedido):
    with connections['mi_db_2'].cursor() as cursor:
        
        sql = """
                select count(NumeroPedido) from EB_TrackDetallePedidos_Mob
                WHERE NumeroPedido LIKE '%"""+ pedido + "'"""
        
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