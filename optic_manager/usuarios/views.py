from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Paciente, Pedido, Producto, Turno, Diagnostico
import datetime, time
from django.core import serializers

# Create your views here.
# pylint: disable=E1101

def welcome_page(request):
    return render (request, "usuarios/welcome.html")


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
                    estado="Pendiente",
                    producto= Producto.objects.get(id=request.POST['id_producto']),
                    precio= request.POST['precio'],
                )
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
            if request.method == "POST":
                paciente_a_editar = Paciente.objects.get(id=request.POST['id_paciente'])
                paciente_a_editar.nombre = request.POST['nuevo_nombre']
                paciente_a_editar.apellido = request.POST['nuevo_apellido']
                paciente_a_editar.dni = request.POST['nuevo_dni']
                paciente_a_editar.telefono = request.POST['nuevo_telefono']
                paciente_a_editar.email = request.POST['nuevo_mail']
                paciente_a_editar.fecha_nacimiento = request.POST['nueva_fecha']
                paciente_a_editar.save()
                
                return render(request, 'usuarios/editar_paciente.html', {
                "pacientes": Paciente.objects.all(),
                "pacientes_serializ": serializers.serialize("json", Paciente.objects.all()), 
            })

            return render(request, 'usuarios/editar_paciente.html', {
                "pacientes": Paciente.objects.all(),
                "pacientes_serializ": serializers.serialize("json", Paciente.objects.all()), 
            })
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
            id_medico = request.session['_auth_user_id']
            medico = User.objects.get(id=id_medico)
            turnos_med = Turno.objects.filter(medico=id_medico)
            return render(request, 'usuarios/turnos_med.html', {
                "medico": medico,
                "turnos": turnos_med,
                "turnos_serializ": serializers.serialize("json", turnos_med),
                "pacientes_serializ": serializers.serialize("json", Paciente.objects.all()),
                "users": serializers.serialize("json", User.objects.all()),
            })

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
                turnos_hoy = Turno.objects.filter(fecha=datetime.date.today())

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

            turnos = Turno.objects.all()
            hoy = datetime.date.today()
            semana = datetime.timedelta(days=7)
            mes = datetime.timedelta(days=30)
            año = datetime.timedelta(days=365)
            años = datetime.timedelta(days=3650)

            if request.method == "POST":
                turno_a_editar = Turno.objects.get(id=request.POST["id_turno"])
                turno_a_editar.medico = User.objects.get(id=request.POST["medico"])
                turno_a_editar.fecha = request.POST["fecha"]
                turno_a_editar.horario = request.POST["horario"]
                turno_a_editar.asistencia = ""
                turno_a_editar.save()
                
                return render(request, "usuarios/editar_turnos.html", {
                "turnos": turnos,
                "turnos_serializados": serializers.serialize("json", turnos),
                "turnos_futuros_sem": turnos.filter(fecha__range=[hoy, hoy + semana]),
                "turnos_futuros_mes": turnos.filter(fecha__range=[hoy, hoy + mes]),
                "turnos_futuros_ano": turnos.filter(fecha__range=[hoy, hoy + año]),
                "pacientes_serializ": serializers.serialize("json", Paciente.objects.all()),
                "medicos": User.objects.filter(groups__name='Profesional medico'),
                "users": serializers.serialize("json", User.objects.all()),
                "turnos_futuros_serializ": serializers.serialize("json", turnos.filter(fecha__range=[hoy, hoy + años]))
            })

            return render(request, "usuarios/editar_turnos.html", {
                "turnos": turnos,
                "turnos_serializados": serializers.serialize("json", turnos),
                "turnos_futuros_sem": turnos.filter(fecha__range=[hoy, hoy + semana]),
                "turnos_futuros_mes": turnos.filter(fecha__range=[hoy, hoy + mes]),
                "turnos_futuros_ano": turnos.filter(fecha__range=[hoy, hoy + año]),
                "pacientes_serializ": serializers.serialize("json", Paciente.objects.all()),
                "medicos": User.objects.filter(groups__name='Profesional medico'),
                "users": serializers.serialize("json", User.objects.all()),
                "turnos_futuros_serializ": serializers.serialize("json", turnos.filter(fecha__range=[hoy, hoy + años]))
            })

def diagnosticar_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Profesional medico':
            print("render diagnosticar")
            id_medico = request.session['_auth_user_id']
            medico = User.objects.get(id=id_medico)
            hoy = datetime.date.today()
            turnos_med_hoy = Turno.objects.filter(medico=id_medico, fecha=hoy)
            if request.method == "POST":
                if Diagnostico.objects.filter(turno_id=request.POST['id_turno']) in Diagnostico.objects.all():
                    return render(request, 'usuarios/diagnosticar.html', {
                        "medico": medico,
                        "hoy": hoy,
                        "turnos": turnos_med_hoy,
                        "mensaje_existe": "El turno seleccionado ya tiene un diagnóstico, puede verlo en el historial del paciente. Por favor seleccione otro turno",
                    })
                else:
                    nuevo_diag = Diagnostico(
                        turno= Turno.objects.get(id=request.POST['id_turno']),
                        diagnostico=request.POST['diagnostico'],
                        observacion = request.POST['observaciones']
                    )
                    nuevo_diag.save()

                    return render(request, 'usuarios/diagnosticar.html', {
                        "medico": medico,
                        "hoy": hoy,
                        "turnos": turnos_med_hoy,
                    })
                
            return render(request, 'usuarios/diagnosticar.html', {
                "medico": medico,
                "hoy": hoy,
                "turnos": turnos_med_hoy,
            })

def pacientes_med_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Profesional medico':
            print("render pacientes_med")
            medico = User.objects.get(id=request.session['_auth_user_id'])
            turnos_med = Turno.objects.filter(medico=request.session['_auth_user_id'])
            pacientes_med=[]
            for turno in turnos_med:
                if turno.paciente not in pacientes_med:
                    pacientes_med.append(turno.paciente)
            fecha_desde = ""
            fecha_hasta = ""
            
            if request.method == "POST":
                if request.POST["submit"] == "BUSCAR":
                    dni = int(request.POST["dni1"])
                    paciente_elegido = Paciente.objects.get(dni=dni)
                    turnos = Turno.objects.filter(paciente=paciente_elegido.id)
                elif request.POST["submit"] == "SELECCIONAR":
                    dni = int(request.POST["dni2"])
                    paciente_elegido = Paciente.objects.get(dni=dni)
                    turnos= Turno.objects.filter(paciente=paciente_elegido.id)
                #if paciente_elegido in pacientes_med:
                if request.POST["submit"] == "FILTRAR":
                    dni = int(request.POST["dni3"])
                    paciente_elegido = Paciente.objects.get(dni=dni)
                    fecha_desde= request.POST["desde"]
                    fecha_hasta=request.POST["hasta"]
                    fecha_desde_format = datetime.datetime.strptime(fecha_desde, '%Y-%m-%d')
                    fecha_hasta_format = datetime.datetime.strptime(fecha_hasta, '%Y-%m-%d') 
                    turnos = Turno.objects.filter(paciente=paciente_elegido.id, fecha__range=[fecha_desde_format, fecha_hasta_format + datetime.timedelta(days=1)])
                    
                return render (request, 'usuarios/pacientes_medV2.html',{
                    "medico": medico,
                    "pacientes": pacientes_med,
                    "diagnosticos": Diagnostico.objects.all(),
                    "turnos": turnos,
                    "paciente_elegido": paciente_elegido,
                    "id_paciente": paciente_elegido.id,
                    "fecha_desde": fecha_desde,
                    "fecha_hasta": fecha_hasta,
                })
                
            return render(request, 'usuarios/pacientes_medV2.html',{
                "medico": medico,
                "pacientes": pacientes_med,
                "diagnosticos": Diagnostico.objects.all(),
                "turnos": "",
                "paciente_elegido": "" ,
                "id_paciente": "",
                "fecha_desde": fecha_desde,
                "fecha_hasta": fecha_hasta,
            })

def ver_pedidos_view (request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Ventas':
            print("render ver_pedidos")
            if request.method == "POST":
                fecha_desde = datetime.datetime.strptime(request.POST["desde"], '%Y-%m-%d')
                fecha_hasta = datetime.datetime.strptime(request.POST["hasta"], '%Y-%m-%d') 
                estado = request.POST["filtro_est"]
                vendedor = request.POST["filtro_vend"]
                paciente = request.POST["filtro_pac"]

                pedidos_fecha = Pedido.objects.filter(fecha_hora__range=[fecha_desde, fecha_hasta + datetime.timedelta(days=1)])

                if estado == "Todos":
                    pedidos_estado = Pedido.objects.all()
                else:
                    pedidos_estado = Pedido.objects.filter(estado=estado)
           
                filtro1 = list(set(pedidos_fecha).intersection(pedidos_estado))
                    
                if vendedor == "Todos":
                    pedidos_vendedor = Pedido.objects.all()
                else:
                    pedidos_vendedor = Pedido.objects.filter(vendedor_id=vendedor)
                    
                if paciente == "Todos":
                    pedidos_paciente = Pedido.objects.all()
                else:
                    pedidos_paciente = Pedido.objects.filter(paciente_id=paciente)
                    
                filtro2 = list(set(pedidos_vendedor).intersection(pedidos_paciente))
                pedidos_filtrados= list(set(filtro1).intersection(filtro2))
                 
                if request.POST["submit"] == "Guardar cambios":
                    for pedido in pedidos_filtrados:
                        pedido = Pedido.objects.get(id=request.POST["ped_id"+str(pedido.id)])
                        pedido.estado = request.POST["ped_est"+str(pedido.id)]
                        pedido.save()
                
                pedidos_fecha = Pedido.objects.filter(fecha_hora__range=[fecha_desde, fecha_hasta + datetime.timedelta(days=1)])
                if estado == "Todos":
                    pedidos_estado = Pedido.objects.all()
                else:
                    pedidos_estado = Pedido.objects.filter(estado=estado)
                filtro1 = list(set(pedidos_fecha).intersection(pedidos_estado))
                if vendedor == "Todos":
                    pedidos_vendedor = Pedido.objects.all()
                else:
                    pedidos_vendedor = Pedido.objects.filter(vendedor_id=vendedor)
                if paciente == "Todos":
                    pedidos_paciente = Pedido.objects.all()
                else:
                    pedidos_paciente = Pedido.objects.filter(paciente_id=paciente)
                filtro2 = list(set(pedidos_vendedor).intersection(pedidos_paciente))
                pedidos_filtrados= list(set(filtro1).intersection(filtro2))

                return render (request, "usuarios/ver_pedidosV2.html",{
                    "fecha_desde": request.POST["desde"],
                    "fecha_hasta": request.POST["hasta"],
                    "filtro_estado": request.POST["filtro_est"],
                    "filtro_vendedor": request.POST["filtro_vend"],
                    "filtro_paciente": request.POST["filtro_pac"],
                    "vendedores": User.objects.filter(groups__name='Ventas'),
                    "pacientes": Paciente.objects.all(),
                    "pedidos": Pedido.objects.all(),
                    "productos": Producto.objects.all(),
                    "pedidos_filtrados": pedidos_filtrados,
                    "pedidos_serializ": serializers.serialize('json', pedidos_filtrados)
                })


            return render(request, "usuarios/ver_pedidosV2.html",{
                "fecha_desde": time.strftime('%Y-%m-%d'),
                "fecha_hasta": time.strftime('%Y-%m-%d'),
                "filtro_estado": "Todos",
                "filtro_vendedor": "Todos",
                "filtro_paciente": "Todos",
                "vendedores": User.objects.filter(groups__name='Ventas'),
                "pacientes": Paciente.objects.all(),
                "pedidos": Pedido.objects.all(),
                "productos": Producto.objects.all(),
                "pedidos_filtrados": Pedido.objects.filter(fecha_hora__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)]),
                "pedidos_serializ": serializers.serialize('json', Pedido.objects.filter(fecha_hora__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)]))
            })

def gerencia_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Gerencia':
            print("render gerencia.html")
            return render(request, "usuarios/gerencia.html",{})

def taller_view(request):
    if 'grupo' in request.session:
        grupo = request.session['grupo']
        print("GRUPO = " + grupo)
        if grupo == 'Taller':
            print("render taller.html")
            return render(request, "usuarios/taller.html",{})

# pylint: enable=E1101    
    