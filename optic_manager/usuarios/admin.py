from django.contrib import admin

from .models import Paciente, Turno, Pedido, Producto, Diagnostico

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Diagnostico)