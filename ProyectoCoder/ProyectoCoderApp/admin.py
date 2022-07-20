from django.contrib import admin

from .models import *

# Register your models here.
    

class VehiculoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo', 'anio', 'precio', 'imagen')
    
   
    
class RepuestoAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo')



class AccesorioAdmin(admin.ModelAdmin):

    list_display = ('marca', 'modelo', 'precio', 'imagen')
    
    

class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'telefono', 'email')
    
    
    
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("usuario", "imagen")

class ResenaAdmin(admin.ModelAdmin):
    list_display = ("idvehiculo", "nombre","telefono","email","fecha","comentario")


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Repuesto, RepuestoAdmin)
admin.site.register(Accesorio, AccesorioAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Resena, ResenaAdmin)

# nacho, admin -> python manage.py createsuperuser