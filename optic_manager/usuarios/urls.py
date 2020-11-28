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
    path("diagnosticar", views.diagnosticar_view, name="diagnosticar"),
    path("pacientes_med", views.pacientes_med_view, name="pacientes_med"),
    path("ver_pedidos", views.ver_pedidos_view, name="ver_pedidos"),
    path("reporte_1", views.reporte_1_view, name="reporte_1"),
    path("reporte_2", views.reporte_2_view, name="reporte_2"),
    path("reporte_3", views.reporte_3_view, name="reporte_3"),
    path("reporte_4", views.reporte_4_view, name="reporte_4"),
    path("taller", views.taller_view, name="taller"),
    path("ver_productos", views.ver_productos_view, name="ver_productos"),
    path("ver_pacientes", views.ver_pacientes_view, name="ver_pacientes"),
    path("nuevo_producto", views.nuevo_producto_view, name="nuevo_producto")
]