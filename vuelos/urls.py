from django.urls import path, include
from . import views

app_name = "vuelos"
urlpatterns = [
    path('', views.index, name="index"),
]