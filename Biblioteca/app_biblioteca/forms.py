from django import forms

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
