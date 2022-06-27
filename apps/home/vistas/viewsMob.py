from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
def Plantilla_Mob(request):
    # Nombre='Despachos pendientes'
    # dir_iframe = DIR_REPORTES['Pedidos_pendiente_despacho']
    return render(request,'home/layout-mob.html')
    # return render(request,'home/layout-top-nav-sidebar.html')