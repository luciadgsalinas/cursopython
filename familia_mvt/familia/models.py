from django.db import models

# Create your models here.
class familia_datos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=60)
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()