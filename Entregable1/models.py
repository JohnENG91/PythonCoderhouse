# Create your models here.

from django.db import models

class modelo_familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    celular = models.IntegerField()
    horario_consulta = models.DateField()