from django import views
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),path('about', views.about, name='about'),
    path('novedades', views.noticias, name='novedades'),
    path('contacto', views.contacto, name='contacto'),
    path('agregar_avatar', views.agregar_avatar, name='agregar_avatar'),
    
    path('vehiculos/', vehiculos, name='vehiculos'),
    path('ingresar_vehiculo/', ingresar_vehiculo, name='ingresar_vehiculo'),
    path('resena_vehiculo/<vehiculo_id>', resena_vehiculo, name='resena_vehiculo'),
    path('eliminar_resena/<resena_id>/<vehiculo_id>', views.eliminar_resena, name='eliminar_resena'),
    path('eliminar_vehiculo/<vehiculo_id>', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('editar_vehiculo/<vehiculo_id>', views.editar_vehiculo, name='editar_vehiculo'),
    
    path('repuestos/', repuesto, name='repuestos'),
    path('ingresar_repuesto/', ingresar_repuesto, name='ingresar_repuesto'),
    path('eliminar_repuesto/<repuesto_id>', views.eliminar_repuesto, name='eliminar_repuesto'),
    path('editar_repuesto/<repuesto_id>', views.editar_repuesto, name='editar_repuesto'),

    path('accesorios/', accesorios, name='accesorios'),
    path('ingresar_accesorio/', ingresar_accesorio, name='ingresar_accesorio'),
    path('eliminar_accesorio/<accesorio_id>', views.eliminar_accesorio, name='eliminar_accesorio'),
    path('editar_accesorio/<accesorio_id>', views.editar_accesorio, name='editar_accesorio'),
    
    path('empleados/', empleados, name='empleados'),
    path('ingresar_empleado/', ingresar_empleado, name='ingresar_empleado'),
    path('eliminar_empleado/<empleado_id>', views.eliminar_empleado, name='eliminar_empleado'),
    path('editar_empleado/<empleado_id>', views.editar_empleado, name='editar_empleado'),
    
    
    
    
    path('contacto/', contacto, name='contacto'),
    
    
    

    
    path('base/', base),
]
