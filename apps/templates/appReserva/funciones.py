from reservarsala.models import reservaSala
# import sys
# import os
# from unipath import Path

# # Obtener ruta del directorio actual
# ruta_actual = os.getcwd()

# # Agregue el directorio donde tiene su función a sys.path
# # sys.path.append(ruta_actual)
# sys.path.append(ruta_actual + '\django-dashboard-adminlte\reservarsala')
# BASE_DIR = Path(__file__).parent
# CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path)
# print(ruta_actual)
# print(BASE_DIR)
# print(CORE_DIR)

reserva = reservaSala.objects.all()
print(reserva)

def cargarEventos():
    turnos=[]
    # eventos={}
    diccionario={'title':'', 'start':'', 'end':'','backgroundColor':'', 'borderColor':'','allDay':''}
    reserva = reservaSala.objects.all()
    for turno in reserva:
        diccionario['title']=turno.titulo
        y=turno.fecha_inicio.strftime("%Y")
        m=turno.fecha_inicio.strftime("%m")
        d=turno.fecha_inicio.strftime("%d")
        h=turno.fecha_inicio.strftime("%H")
        mi=turno.fecha_inicio.strftime("%M")
        diccionario['start']='new Date('+y+','+m+','+d+','+h+','+mi+')'
        y=turno.fecha_fin.strftime("%Y")
        m=turno.fecha_fin.strftime("%m")
        d=turno.fecha_fin.strftime("%d")
        h=turno.fecha_fin.strftime("%H")
        mi=turno.fecha_fin.strftime("%M")
        diccionario['end']='new Date('+y+','+m+','+d+','+h+','+mi+')'
        diccionario['backgroundColor']=turno.backgroundColor
        diccionario['borderColor']=turno.borderColor
        diccionario['allDay']=turno.allDay
        turnos.append(diccionario)

    print(turnos)


# setEventos={
#         'plugins': [ 'bootstrap', 'interaction', 'dayGrid', 'timeGrid' ],
#         'header' : {
#           'left'  : 'prev,next today',
#           'center': 'title',
#           'right' : 'dayGridMonth,timeGridWeek,timeGridDay'
#         },
#         'themeSystem': 'bootstrap',
#         # //Random default events
        
#         'events': '',
#         'editable': 'true',
#         'droppable': 'true', """ // this allows things to be dropped onto the calendar !!! """
#         'drop': 'function(info) {if (checkbox.checked) {info.draggedEl.parentNode.removeChild(info.draggedEl);}}'
#       }