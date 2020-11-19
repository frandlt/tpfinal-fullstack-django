from django.shortcuts import render
#from sistema.models import 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render (request,"sistema/index.html")