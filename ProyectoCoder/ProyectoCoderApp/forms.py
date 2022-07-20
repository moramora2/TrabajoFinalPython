from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
    
class NuevoVehiculo(forms.Form):
    marca = forms.CharField(label="Marca", widget=forms.TextInput(attrs={'class': "form-control"}))
    modelo = forms.CharField(max_length=30,label="Modelo", widget=forms.TextInput(attrs={'class': "form-control"}))
    anio = forms.IntegerField(min_value=1900,label="Año", widget=forms.TextInput(attrs={'class': "form-control"}))
    precio = forms.IntegerField(min_value=1,label="Precio", widget=forms.TextInput(attrs={'class': "form-control"}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}))
    

class NuevaResena(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(max_length=30,label="Email", widget=forms.TextInput(attrs={'class': "form-control"}))
    telefono = forms.CharField(max_length=30,label="Telefono", widget=forms.TextInput(attrs={'class': "form-control"}))
    comentario = forms.CharField(max_length=300,label="Comentario", widget=forms.TextInput(attrs={'class': "form-control"}))
    
class NuevoRepuesto(forms.Form):
    marca = forms.CharField(max_length=30,label="Marca", widget=forms.TextInput(attrs={'class': "form-control"}))
    modelo = forms.CharField(max_length=30,label="Modelo", widget=forms.TextInput(attrs={'class': "form-control"}))

    
class NuevoAccesorio(forms.Form):
    marca = forms.CharField(max_length=30,label="Marca", widget=forms.TextInput(attrs={'class': "form-control"}))
    modelo = forms.CharField(max_length=30,label="Modelo", widget=forms.TextInput(attrs={'class': "form-control"}))
    precio = forms.IntegerField(min_value=1,label="Precio",widget=forms.TextInput(attrs={'class': "form-control"}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}))
    
class NuevoEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre", widget=forms.TextInput(attrs={'class': "form-control"}))
    apellido = forms.CharField(max_length=30,label="Apellido", widget=forms.TextInput(attrs={'class': "form-control"}))
    telefono = forms.IntegerField(label="Telefono", widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="Correo electronico")
    
    

class UserRegisterForm(UserCreationForm):

    avatar = forms.ImageField(label="Avatar", required=False)
    email= forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["avatar","username", "email", "password1", "password2", "first_name", "last_name"]


class UserEditForm(UserCreationForm):

    avatar = forms.ImageField(label="Avatar", required=False)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput, required= False)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput, required= False) 
    first_name = forms.CharField(label="Nombre", required= False)
    last_name = forms.CharField(label="Apellido", required= False)

    class Meta:
        model = User
        fields = ["avatar","email", "password1", "password2", "first_name", "last_name"]

        help_texts = {k: "" for k in fields}    
        
        
        
class FormAvatar(ModelForm):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        