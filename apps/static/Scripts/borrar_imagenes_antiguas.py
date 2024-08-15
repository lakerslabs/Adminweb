import os
import time
import logging
from datetime import datetime, timedelta

# Configurar el logging
logging.basicConfig(filename='log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Directorio donde se encuentran las imágenes
directorio = r'C:\Users\eduardo.berga\Desktop\Proyectos\Lakers_Lab\Adminweb\media\images'

# Tiempo límite (3 días en segundos)
tiempo_limite = 90 * 24 * 60 * 60

def borrar_imagenes_antiguas():
    try:
        ahora = time.time()
        for filename in os.listdir(directorio):
            ruta_archivo = os.path.join(directorio, filename)
            if os.path.isfile(ruta_archivo):
                tiempo_creacion = os.path.getmtime(ruta_archivo)
                if ahora - tiempo_creacion > tiempo_limite:
                    try:
                        os.remove(ruta_archivo)
                        print(f"Archivo borrado: {filename}")
                    except Exception as e:
                        logging.error(f"No se pudo borrar el archivo {filename}: {str(e)}")
    except Exception as e:
        logging.error(f"Error al acceder al directorio o procesar archivos: {str(e)}")

if __name__ == "__main__":
    borrar_imagenes_antiguas()
    print("Proceso completado. Revise el archivo log.txt para ver si hubo errores.")
