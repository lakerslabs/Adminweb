import django
from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class reservaSala(models.Model):
    usuario_id=models.AutoField(primary_key=True,unique=True,auto_created=True,editable=False)
    titulo = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(verbose_name='Inicio')
    fecha_fin = models.DateTimeField(verbose_name='Fin')
    backgroundColor = models.CharField(max_length=50,default='#f39c12',verbose_name='Color de fondo')
    borderColor = models.CharField(max_length=50,default='#f39c12',verbose_name='Color de borde')
    allDay = models.BooleanField(default=False,blank=True)
    creador = models.ForeignKey(
        User,
        default=User,
        on_delete=models.CASCADE,
        editable=True,
        blank=True,
        null=True,
        db_column='autor_id',

    )
       
    def __str__(self):
        return self.titulo