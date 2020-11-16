from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request, grupo):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "usuarios/usuario.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print("log:"+str(request))
        if user is not None:
            login(request, user)
            grupo = str(user.groups.values_list('name', flat=True).first())
            #print(grupo)
            return render(request, "usuarios/usuario.html", { 'grupo': grupo } )
        else:
            return render(request, "usuarios/login.html", {
                "mensaje": "Credenciales no validas."
            })
    else:
        return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {
        "mensaje": "Desconectado."
    })

#def ejemplo_view(request):
#    return HttpResponse()

#ef is_ventas(user):
#        return user.groups.filter(name='Ventas').exists()

        #for e in user.groups.values_list():
            #    print("e2 :" + str(e))