from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("generar_pedido", views.generar_pedido_view, name="generar_pedido"),
    path("generar_turno", views.generar_turno_view, name="generar_turno"),
    path("editar_paciente", views.editar_paciente_view, name="editar_paciente")
]