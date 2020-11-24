from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Paciente, Pedido, Producto, Turno, Diagnostico
import datetime
from django.core import serializers

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if 'grupo' not in request.session:
        grupo = request.session['grupo'] 
        print("REQUEST.SESSION = " + grupo)
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
            
            lentes = []
            for i in range (1,9):
                lentes.append(Producto.objects.get(id=i))
            otros_productos = [producto for producto in Producto.objects.all() if producto not in lentes]

            if request.method=="POST":
                nuevo_pedido=Pedido(
                    paciente= Paciente.objects.get(dni=request.POST['paciente']),
                    vendedor= User.objects.get(id=request.session['_auth_user_id']),
                    fecha_hora= datetime.datetime.now(),
                    cantidad= request.POST['cantidad'],
                    medio_pago=request.POST['medio_pago'],
                    estado=request.POST['estado'],
                )
                if request.POST['tipo']=="producto":
                    id_prod=request.POST['id-otro']
                elif request.POST['tipo']=="lente":
                    id_prod=request.POST['id-lente']
                else: 
                    mensaje="ERROR: No puede obtenerse el ID del producto"
                    return render(request, 'usuarios/generar_pedido.html', {
                    "nuevo_id": int(Pedido.objects.last().id) + 1,
                    "pacientes": Paciente.objects.all(),
                    "otros_productos":otros_productos,
                    "productos": Producto.objects.all(),
                    "productos_serializados": serializers.serialize("json", Producto.objects.all())
                })
                nuevo_pedido.producto=(Producto.objects.get(id=id_prod))
                nuevo_pedido.precio=(Producto.objects.get(id=id_prod).precio_actual)
                nuevo_pedido.save()

                return render(request, 'usuarios/generar_pedido.html', {
                    "nuevo_id": int(Pedido.objects.last().id) + 1,
                    "pacientes": Paciente.objects.all(),
                    "otros_productos":otros_productos,
                    "productos": Producto.objects.all(),
                    "productos_serializados": serializers.serialize("json", Producto.objects.all())
                })

            
            return render(request, 'usuarios/generar_pedido.html', {
                "nuevo_id": int(Pedido.objects.last().id) + 1,
                "pacientes": Paciente.objects.all(),
                "otros_productos":otros_productos,
                "productos": Producto.objects.all(),
                "productos_serializados": serializers.serialize("json", Producto.objects.all())
            })
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
        return HttpResponseRedirect(reverse("usuario"))

def generar_turno_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Secretaria':
            print("render generar turno")
            if request.method == "POST":
                #si tenemos ganas de complicarla podemos agregar una verificacion para ese horario y medico
                nuevo_turno = Turno(
                    paciente = Paciente.objects.get(dni=request.POST['paciente']),
                    fecha = request.POST['fecha'],
                    horario = request.POST['horario'],
                    medico = User.objects.get(id=request.POST['medico']),
                )
                nuevo_turno.save()
                return render(request, 'usuarios/generar_turno.html', {
                    'medicos': User.objects.filter(groups__name='Profesional medico'),
                    'pacientes': Paciente.objects.all(),
                    'mensaje_exito':'Turno registrado con éxito!'
                })
            else:
                return render(request, 'usuarios/generar_turno.html', {
                    'medicos': User.objects.filter(groups__name='Profesional medico'),
                    'pacientes': Paciente.objects.all()
                })
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
        return HttpResponseRedirect(reverse("usuario"))

def editar_paciente_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Secretaria':
            print("render editar paciente")
            return render(request, 'usuarios/editar_paciente.html', {})
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
        return HttpResponseRedirect(reverse("usuario"))

def turnos_med_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Profesional medico':
            print("render turnos_med")
            return render(request, 'usuarios/turnos_med.html', {})
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
        return HttpResponseRedirect(reverse("usuario"))


def agregar_paciente_view(request): 
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Secretaria':
            print("render agregar paciente")
            if request.method == 'POST':
                dnis_existentes = []
                for paciente in Paciente.objects.all():
                    dnis_existentes.append(paciente.dni)
                if int(request.POST['dni']) in dnis_existentes:
                    return render(request, "usuarios/agregar_paciente.html",{
                        "mensaje_existe": "El paciente con ese numero de documento ya existe."
                    })
                else: 
                    nuevo_paciente = Paciente(
                        nombre=request.POST['nombre'],
                        apellido=request.POST['apellido'],
                        dni=request.POST['dni'],
                        fecha_nacimiento=request.POST['fec_nac'],
                        email=request.POST['mail'],
                        telefono=request.POST['telefono'],
                    )
                    nuevo_paciente.save()
                    return render(request, "usuarios/agregar_paciente.html",{
                        "mensaje_exito": "Nuevo paciente creado con exito!"
                    })
            else:
                return render(request, "usuarios/agregar_paciente.html")
        else:
            return HttpResponseRedirect(reverse("usuario"))
    else:
            return HttpResponseRedirect(reverse("usuario"))

def turnos_hoy_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Secretaria':
            print("render turnos hoy")
            turnos_hoy = Turno.objects.filter(fecha=datetime.date.today())
            #turnos_jane = Turno.objects.filter(paciente_id="2")
            #print("turnos_jane = " + str(turnos_jane))
            if request.method == "POST":
                for i in range(1,len(turnos_hoy)+1):
                    print("i = " + str(i))
                    turno = Turno.objects.get(id=request.POST["id-"+str(i)])
                    turno.asistencia = request.POST["asist-"+str(i)]
                    turno.save()
                    i+=1

            return render(request, "usuarios/turnos_hoy.html", {
                "turnos_hoy": turnos_hoy,
                "turnos_serializados": serializers.serialize("json", turnos_hoy),
            })

def editar_turnos_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Secretaria':
            print("editar turnos")
            return render(request, "usuarios/editar_turnos.html", {})

            