import requests
import json
import os



# Reemplaza con tu API Key y Token
API_KEY = ''
API_TOKEN = ''
BOARD_ID = ''

# URL base de la API de Trello
BASE_URL = 'https://api.trello.com/1/'

# Función para obtener la información del tablero
def get_board_info(board_id):
    url = f"{BASE_URL}boards/{board_id}"
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'fields': 'name,desc,closed,idOrganization,prefs'
    }
    response = requests.get(url, params=query)
    return response.json()

# Función para obtener las listas del tablero
def get_lists(board_id):
    url = f"{BASE_URL}boards/{board_id}/lists"
    query = {
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.get(url, params=query)
    return response.json()

# Función para obtener las tarjetas de una lista
def get_cards(list_id):
    url = f"{BASE_URL}lists/{list_id}/cards"
    query = {
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.get(url, params=query)
    return response.json()

# Función para obtener las acciones de una tarjeta
def get_card_actions(card_id):
    url = f"{BASE_URL}cards/{card_id}/actions"
    query = {
        'key': API_KEY,
        'token': API_TOKEN
    }
    response = requests.get(url, params=query)
    return response.json()

# Obtener la información del tablero
board_info = get_board_info(BOARD_ID)

# Obtener todas las listas del tablero
lists = get_lists(BOARD_ID)

# Crear un reporte con toda la información del tablero
report = {
    'Tablero': board_info,
    'Listas': []
}

for list in lists:
    cards = get_cards(list['id'])
    list_info = {
        'Lista': list,
        'Tarjetas': []
    }
    for card in cards:
        actions = get_card_actions(card['id'])
        list_info['Tarjetas'].append({
            'Tarjeta': card,
            'Acciones': actions
        })
    report['Listas'].append(list_info)

# Establecer la ruta de la carpeta de destino
carpeta_de_destino = r''
destino = os.path.join(carpeta_de_destino, 'reporte_completo_trello_con_acciones.json')
print(destino)

# Crear la carpeta si no existe
if not os.path.exists('carpeta_de_destino'):
    os.makedirs('carpeta_de_destino')

# Guardar el reporte en el archivo JSON
with open(destino, 'w') as f:
    json.dump(report, f, indent=4)

print("Reporte completo con acciones generado exitosamente.")