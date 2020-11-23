from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Paciente (models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    dni = models.PositiveIntegerField(validators=[MaxValueValidator(99999999)])
    fecha_nacimiento= models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Turno (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario= models.TimeField()
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, db_column="medico_id", on_delete=models.CASCADE)
    asistencia = models.CharField(max_length=2, blank=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField(blank=True)
    precio_actual = models.DecimalField(max_digits=8, decimal_places=2)

class Pedido (models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, db_column="vendedor_id", on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad= models.IntegerField()
    #subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    medio_pago = models.CharField(max_length=20)
    estado = models.CharField(max_length=30)

class Diagnostico(models.Model):
    turno=models.OneToOneField(Turno, on_delete=models.CASCADE)
    diagnostico= models.TextField()
    observacion= models.TextField()