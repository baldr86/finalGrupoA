from django.db import models

class Libro(models.Model):
    nombre= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    publicacion= models.DateField()
    genero= models.CharField(max_length=20)
   

class Autor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    nacionalidad= models.CharField(max_length=40)
    cantLibros= models.IntegerField()

class Genero(models.Model):
    generos=["Aventura", "Suspenso", "historia"]
    genero= genero= models.CharField(max_length=20)


