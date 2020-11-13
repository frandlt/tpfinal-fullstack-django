from django.db import models

# Create your models here.
class Vuelo(models.Model):
    origen = models.CharField(max_length=64)
    destino = models.CharField(max_length=64)
    duracion = models.IntegerField()