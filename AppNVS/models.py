from django.db import models
from django.db.models.fields import CharField, IntegerField, DateField
# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fec_nac = models.DateField()