from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Pacientes(models.Model):
    paciente_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dni = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()