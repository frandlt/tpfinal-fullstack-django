from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Paciente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()