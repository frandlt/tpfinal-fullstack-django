from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("generar_pedido", views.generar_pedido_view, name="generar_pedido"),
    path("generar_turno", views.generar_turno_view, name="generar_turno"),
    path("agregar_paciente", views.agregar_paciente_view, name="agregar_paciente"),
    path("editar_paciente", views.editar_paciente_view, name="editar_paciente"),
    path("turnos_med", views.turnos_med_view, name="turnos_med")
]