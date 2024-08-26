from django.db import connections

def validar_factManualCargada(sucursal,factura):
    with connections['mi_db_4'].cursor() as cursor:
        sql = '''
            SET DATEFORMAT DMY 
            DECLARE @COMPROBANTE VARCHAR(14) = ''' + "'" + factura + "'"+''';
            DECLARE @sucursal VARCHAR(5) = ''' + "'" + sucursal + "'"+''';
            DECLARE @terminal VARCHAR(20);
            DECLARE @factura INT;
            SET @terminal = SUBSTRING(@COMPROBANTE, 2, CHARINDEX('-', @COMPROBANTE) - 2);
            SET @factura = CAST(SUBSTRING(@COMPROBANTE, CHARINDEX('-', @COMPROBANTE) + 1, LEN(@COMPROBANTE))AS INT)-1;
            select COUNT(A.NComp) 
            from (
                SELECT CTA02.N_COMP AS NComp 
                FROM 
                CTA02 (NOLOCK)  
                LEFT JOIN CTA_TIPO_COMPROBANTE_VENTAS ON CTA02.T_COMP = CTA_TIPO_COMPROBANTE_VENTAS.IDENT_COMP 
                and CTA02.NRO_SUCURS = CTA_TIPO_COMPROBANTE_VENTAS.NRO_SUCURS  
                LEFT JOIN CTA_VENDEDOR ON CTA02.COD_VENDED = CTA_VENDEDOR.COD_VENDEDOR  
                LEFT JOIN CTA_CLIENTE ON CTA02.COD_CLIENT = CTA_CLIENTE.COD_CLIENTE 
                WHERE
                CTA02.ESTADO <> 'ANU' AND CTA02.T_COMP <> 'REC'  AND CTA02.COD_VENDED <> '**' 
                AND 
                ( (Fecha_Emis BETWEEN '01/01/2024' AND '31/12/2024')) AND TIPO_TALONARIO IN ( 'Manual' )
                AND CTA02.NRO_SUCURS = @sucursal
                AND CTA02.N_COMP LIKE '%'+CAST(@factura AS varchar(10))
                AND SUBSTRING(CTA02.N_COMP, 3, 4) = @terminal
                GROUP BY 
                CTA02.TIPO_TALONARIO , CTA02.TIPO_AUTORIZACION , SUBSTRING(CTA02.N_COMP, 3, 4) , 
                CTA02.T_COMP , CTA02.N_COMP , CTA02.TALONARIO  , CTA_TIPO_COMPROBANTE_VENTAS.DESCRIPCIO , 
                CTA02.IMPORTE , CTA02.NRO_SUCURS , CTA02.FECHA_EMIS
            ) A'''
        cursor.execute(sql)
        # print('Parametros de consulta: ' + str(sucursal) + ' ' + str(factura))
        resulatado = cursor.fetchone()
        # print(resulatado[0])
    return resulatado[0]

def validar_articulo(articulo):
    with connections['mi_db_2'].cursor() as cursor:
        sql = ''' SELECT COALESCE((SELECT TOP 1 DESCRIPCIO FROM SJ_ETIQUETAS_FINAL WHERE COD_ARTICU = ''' + "'" + articulo + "'" + '),' + "'ERROR'" + ") AS RESULT"
        cursor.execute(sql)
        # print(sql)
        resulatado = cursor.fetchone()
        # print(resulatado[0])
    return resulatado[0]

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