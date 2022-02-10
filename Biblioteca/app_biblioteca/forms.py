from pickle import TRUE
from tokenize import group
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentarios

class LibroFormulario(forms.Form):   
    nombre= forms.CharField(max_length=40)
    autor= forms.CharField(max_length=30)
    publicacion= forms.IntegerField()
    genero= forms.CharField(max_length=20)
    editorial= forms.CharField(max_length=20)

class SocioFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    documento= forms.IntegerField()
    mail= forms.EmailField()
    telefono= forms.IntegerField()


class CursoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    codigocurso=forms.IntegerField()
    docente=forms.CharField(max_length=30)
    diahorario=forms.CharField(max_length=40)

class UserRegisterForm (UserCreationForm):

    username= forms.CharField(label='Nombre de usuario')
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    groups = forms.CharField(initial='Asociados', label='Grupo Asociados')
    

    class Meta:

        model= User
        fields = ['username', 'email', 'password1', 'password2', 'groups']
        #saca los mensajes de ayuda
        help_text = {k:"" for k in fields}

#Formularios para Posts

class postForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comentarios
        fields = ('comentario', )