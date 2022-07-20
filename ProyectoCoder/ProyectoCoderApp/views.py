import datetime
import email

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

from .models import Accesorio, Avatar, Vehiculo, Repuesto, Empleado, Resena
from .forms import FormAvatar, NuevoRepuesto, NuevoVehiculo, NuevoAccesorio, NuevoEmpleado, UserRegisterForm, NuevaResena
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import date
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from django.urls import reverse_lazy

# Create your views here.




    
    
    
def vehiculos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            vehiculos = Vehiculo.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/vehiculos.html",{"vehiculos":vehiculos, "search":True, "busqueda":search})

    vehiculos = Vehiculo.objects.all()

    return render(request,"ProyectoCoderApp/vehiculos.html",{"vehiculos":vehiculos, "search":False})




@staff_member_required
def eliminar_resena(request, resena_id, vehiculo_id):

    resena = Resena.objects.get(id=resena_id)
    resena.delete()

    return redirect("resena_vehiculo", vehiculo_id=vehiculo_id)



@login_required
def resena_vehiculo(request, vehiculo_id):
    
    # post
    if request.method == "POST":
        
        formulario = NuevaResena(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            fec = date.today()
            Resenas = Resena(idvehiculo=vehiculo_id,nombre=info["nombre"],telefono=info["telefono"],email=info["email"],comentario=info["comentario"],fecha=fec)
            Resenas.save()

            return redirect("resena_vehiculo", vehiculo_id=vehiculo_id)
        
       
    # get
    resenas = Resena.objects.filter(idvehiculo=vehiculo_id)
    # resenas = Resena.objects.all()
    formulario = NuevaResena()
    return render(request,"ProyectoCoderApp/resena_vehiculo.html",{"resenas":resenas, "form":formulario})
    


@login_required
def ingresar_vehiculo(request):
    
    
    # post
    if request.method == "POST":
        
        formulario = NuevoVehiculo(request.POST, files=request.FILES)

        if formulario.is_valid():
        
            info = formulario.cleaned_data

            vehiculo = Vehiculo(marca=info["marca"],modelo=info["modelo"],anio=info["anio"], precio=info["precio"], imagen=request.FILES["imagen"])
            vehiculo.save()

            return redirect("vehiculos")
        
       
       # get
    formulario = NuevoVehiculo()
    return render(request,"ProyectoCoderApp/vehiculos_form.html",{"form":formulario,"accion":"Ingresar"})


 
    
    
def repuesto(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            repuestos = Repuesto.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/repuestos.html",{"repuestos":repuestos, "search":True, "busqueda":search})

    repuestos = Repuesto.objects.all()

    return render(request,"ProyectoCoderApp/repuestos.html",{"repuestos":repuestos, "search":False})



def ingresar_repuesto(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoRepuesto(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            repuesto = Repuesto(marca=info["marca"],modelo=info["modelo"],)
            repuesto.save()

            return redirect("repuestos")

        return render(request,"ProyectoCoderApp/repuestos_form.html",{"form":formulario,"accion":"Ingresar"})
    
    
           # get
    formulario = NuevoRepuesto()
    return render(request,"ProyectoCoderApp/repuestos_form.html",{"form":formulario,"accion":"Ingresar"})
    
    
    
    
def accesorios(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            acceosrios = Accesorio.objects.filter( Q(marca__icontains=search) | Q(modelo__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/accesorios.html",{"accesorios":accesorios, "search":True, "busqueda":search})

    accesorios = Accesorio.objects.all()

    return render(request,"ProyectoCoderApp/accesorios.html",{"accesorios":accesorios, "search":False})


def ingresar_accesorio(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoAccesorio(request.POST, files=request.FILES)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            accesorio = Accesorio(marca=info["marca"],modelo=info["modelo"],precio=info["precio"], imagen=request.FILES["imagen"])
            accesorio.save()

            return redirect("accesorios")

        return render(request,"ProyectoCoderApp/accesorios_form.html",{"form":accesorio,"accion":"Ingresar"})
    
    
           # get
    formulario = NuevoAccesorio()
    return render(request,"ProyectoCoderApp/accesorios_form.html",{"form":formulario,"accion":"Ingresar"})




def empleados(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            empleados = Empleado.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/empleados.html",{"empleados":empleados, "search":True, "busqueda":search})

    empleados = Empleado.objects.all()
    return render(request,"ProyectoCoderApp/empleados.html",{"empleados":empleados, "search":False})


def ingresar_empleado(request):
    
    # post
    if request.method == "POST":
        
        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            empleado = Empleado(nombre=info["nombre"],apellido=info["apellido"],telefono=info["telefono"], email=info["email"])
            empleado.save()

            return redirect("empleados")

        return render(request,"ProyectoCoderApp/empleados_form.html",{"form":formulario,"accion":"Ingresar"})
    
       # get
    formulario = NuevoEmpleado()
    return render(request,"ProyectoCoderApp/empleados_form.html",{"form":formulario,"accion":"Ingresar"})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def index(request):
    vehiculo = Vehiculo.objects.all()
    empleado = Empleado.objects.all()
    repuesto = Repuesto.objects.all()
    accesorio = Accesorio.objects.all()
    contexto = {"vehiculo": vehiculo, "empleado": empleado, "repuesto": repuesto, "accesorio": accesorio}
    
    return render(request, "ProyectoCoderApp/index.html", contexto)



@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":
        
        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data           
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()
            

            return redirect("index")

    else:
        form = UserEditForm(initial = {"email":user.email, "first_name": user.first_name, "last_name": user.last_name})

    return render(request, "ProyectoCoderApp/editar_perfil.html", {"form": form}) 
    
    
def noticias(request):
    return render(request, 'ProyectoCoderApp/noticias.html')    

def about(request):
    
    return render(request, 'ProyectoCoderApp/about.html')

def contacto(request):

    return render(request, 'ProyectoCoderApp/contacto.html')



def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")
        else:
            return redirect("login")

    form= AuthenticationForm()

    return render(request, "ProyectoCoderApp/login.html", {"form": form})



def logout_request(request):
    
    logout(request)
    return redirect("index")



@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = FormAvatar(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            info = form.cleaned_data
            avatar = Avatar.objects.get(usuario=user)
            avatar.imagen = info["imagen"]
            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("index")

    else:
        form = FormAvatar()
    
    return render(request, "ProyectoCoderApp/agregar_avatar.html", {"form": form})


def register_request(request):

    if request.method == "POST":

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")            

        return render(request, "ProyectoCoderApp/register.html", {"form": form})

    # form= UserCreationForm()
    form= UserRegisterForm() #este sirve para editarlo a nuestra manera

    return render(request, "ProyectoCoderApp/register.html", {"form": form})



@staff_member_required
def eliminar_vehiculo(request, vehiculo_id):

    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    vehiculo.delete()

    return redirect("vehiculos")



@staff_member_required
def eliminar_accesorio(request, accesorio_id):

    accesorio = Accesorio.objects.get(id=accesorio_id)
    accesorio.delete()

    return redirect("accesorios")


@staff_member_required
def eliminar_empleado(request, empleado_id):

    empleado = Empleado.objects.get(id=empleado_id)
    empleado.delete()

    return redirect("empleados")


@staff_member_required
def eliminar_repuesto(request, repuesto_id):

    repuesto = Repuesto.objects.get(id=repuesto_id)
    repuesto.delete()

    return redirect("repuestos")


@staff_member_required
def editar_vehiculo(request, vehiculo_id):

    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    
    if request.method == "POST":
        
        formulario = NuevoVehiculo(request.POST, files=request.FILES)

        if formulario.is_valid():

            info_vehiculo = formulario.cleaned_data

            vehiculo.marca = info_vehiculo["marca"]
            vehiculo.modelo = info_vehiculo["modelo"]
            vehiculo.anio = info_vehiculo["anio"]
            vehiculo.precio = info_vehiculo["precio"]
            vehiculo.imagen = request.FILES["imagen"]
            vehiculo.save()

            return redirect("vehiculos")

    #get
    formulario = NuevoVehiculo(initial= {"marca": vehiculo.marca, "modelo": vehiculo.modelo, "anio": vehiculo.anio, "precio": vehiculo.precio})

    return render(request,"ProyectoCoderApp/vehiculos_form.html",{"form":formulario,"accion":"Editar vehículo"})

@staff_member_required
def editar_empleado(request, empleado_id):

    empleado = Empleado.objects.get(id=empleado_id)
    
    if request.method == "POST":
        
        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():

            info_empleado = formulario.cleaned_data

            empleado.nombre = info_empleado["nombre"]
            empleado.apellido = info_empleado["apellido"]            
            empleado.email = info_empleado["email"]
            empleado.telefono = info_empleado["telefono"]
            empleado.save()

            return redirect("empleados")

    #get
    formulario = NuevoEmpleado(initial= {"nombre": empleado.nombre, "apellido": empleado.apellido, "email": empleado.email, "telefono": empleado.telefono})
 

    return render(request,"ProyectoCoderApp/empleados_form.html",{"form":formulario,"accion":"Editar empleados"})


def editar_accesorio(request, accesorio_id):

    accesorio = Accesorio.objects.get(id=accesorio_id)
    
    if request.method == "POST":
        
        formulario = NuevoAccesorio(request.POST)

        if formulario.is_valid():

            info_accesorio = formulario.cleaned_data

            accesorio.marca = info_accesorio["marca"]
            accesorio.modelo = info_accesorio["modelo"]            
            accesorio.precio = info_accesorio["precio"]
            accesorio.save()

            return redirect("accesorios")

    #get
    formulario = NuevoAccesorio(initial= {"marca": accesorio.marca, "modelo": accesorio.modelo, "precio": accesorio.precio})

    return render(request,"ProyectoCoderApp/accesorios_form.html",{"form":formulario,"accion":"Editar accesorio"})



@staff_member_required
def editar_repuesto(request, repuesto_id):

    repuesto = Repuesto.objects.get(id=repuesto_id)
    
    if request.method == "POST":
        
        formulario = NuevoRepuesto(request.POST)

        if formulario.is_valid():

            info_repuesto = formulario.cleaned_data

            repuesto.marca = info_repuesto["marca"]
            repuesto.modelo = info_repuesto["modelo"]
            repuesto.save()

            return redirect("repuestos")

    #get
    formulario = NuevoRepuesto(initial= {"marca": repuesto.marca, "modelo": repuesto.modelo})
    

    return render(request,"ProyectoCoderApp/repuestos_form.html",{"form":formulario,"accion":"Editar repuesto"})

