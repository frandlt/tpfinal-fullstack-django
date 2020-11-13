from django.shortcuts import render
from django.http import HttpResponseRedirect

Prueba = ["despertarme", "ordenar el cuarto", "barrer el piso", "ir a la tienda"]

# Create your views here.
def index(request):
    return render(request, "index.html")