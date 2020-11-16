from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if 'grupo' not in request.session:
        request.session['grupo'] = grupo
        print("REQUEST.SESSION = " + request.session['grupo'])
        return render(request, "usuarios/usuario.html", {
            'grupo': request.session['grupo']
        })
    else:
        return render(request, "usuarios/usuario.html", {
            'grupo': request.session['grupo']
        })
        #return render(request, "usuarios/usuario.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print("log:"+str(request))
        if user is not None:
            login(request, user)
            grupo = str(user.groups.values_list('name', flat=True).first())
            request.session['grupo'] = grupo
            print(grupo)
            print(request.session['grupo'])
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

def generar_pedido_view(request):
    #print("USERNAME = " + request.user.username)
    #print("GRUPO = " + grupo)
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Ventas':
            return render(request, 'usuarios/generar_pedido.html', {})
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
        return HttpResponseRedirect(reverse("usuario"))

#def ejemplo_view(request):
#    return HttpResponse()

#ef is_ventas(user):
#        return user.groups.filter(name='Ventas').exists()

        #for e in user.groups.values_list():
            #    print("e2 :" + str(e))