from django.db import models
from django.db.models.base import Model

# Create your models here.

class Transporte(models.Model):
    COD_TRANSP = models.CharField(primary_key=True, max_length=4)
    NOMBRE = models.CharField(max_length=50)
    COSTE_BULTO = models.DecimalField(max_digits=10, decimal_places=2)
    COSTE_SEGURO = models.DecimalField(max_digits=10, decimal_places=2)
    COSTE_RETIRO = models.DecimalField(max_digits=10, decimal_places=2)
    COSTE_ENTREGA = models.DecimalField(max_digits=10, decimal_places=2)
    RETIRA_EN_CD = models.BooleanField(default=False,blank=True)
    OBSERVASIONES = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.NOMBRE
