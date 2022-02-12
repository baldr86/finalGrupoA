from pickle import TRUE
from tokenize import group
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comentarios

class UserRegisterForm (UserCreationForm):

    username= forms.CharField(label='Nombre de usuario')
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
   
    

    class Meta:

        model= User
        fields = ['username', 'email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_text = {k:"" for k in fields}

#Formularios para Posts

class postForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('titulo', 'contenido', 'imagen', "autor")
        

class CommentForm(forms.ModelForm):

    class Meta:

        model = Comentarios
        fields = ('comentario', )