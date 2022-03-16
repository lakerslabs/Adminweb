from django.shortcuts import render

def transporte(request):
    return render(request, 'django-dashboard-adminlte/Transportes/templates/gestionTransporte.html')