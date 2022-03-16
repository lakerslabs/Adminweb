import sys
import os
from unipath import Path

# Obtener ruta del directorio actual
ruta_actual = os.getcwd()

# Agregue el directorio donde tiene su función a sys.path
# sys.path.append(ruta_actual)
sys.path.append(ruta_actual + '\django-dashboard-adminlte\reservarsala')
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
print(ruta_actual)
print(BASE_DIR)
print(CORE_DIR)