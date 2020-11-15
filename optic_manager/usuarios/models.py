from django.db import models

# Create your models here.
class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()

 #   def __str__(self):
 #       return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    medico_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
#    pacientes_asignados = models.ManyToManyField(Paciente, blank=True, related_name="paciente_id")

 #   def __str__(self):
 #       return f"{self.nombre} {self.apellido}"

#class Historial(models.Model):
#    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="paciente_id")
#    medico_asignado = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="medico_asignado")
#    observaciones = models.CharField(max_length=1024)
#
#    def __str__(self):
#        return f"{self.paciente_id} {self.medico_asignado}"