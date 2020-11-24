from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome_page, name="welcome_page"),
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("generar_pedido", views.generar_pedido_view, name="generar_pedido"),
    path("generar_turno", views.generar_turno_view, name="generar_turno"),
    path("editar_paciente", views.editar_paciente_view, name="editar_paciente"),
    path("turnos_med", views.turnos_med_view, name="turnos_med"),
    path("agregar_paciente", views.agregar_paciente_view, name="agregar_paciente"),
    path("turnos_hoy", views.turnos_hoy_view, name="turnos_hoy"),
    path("editar_turnos", views.editar_turnos_view, name="editar_turnos"),
]