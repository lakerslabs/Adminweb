from django.urls import path
from Transportes import views

urlpatterns = [

    # The home page
    path('transporte', views.transporte, name='transporte'),

   

]
