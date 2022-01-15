from django.db import models

class Libro(models.Model):
    nombre= models.CharField(max_length=40)
    autor= models.CharField(max_length=30)
    publicacion= models.IntegerField()
    genero= models.CharField(max_length=20)
    editorial=models.CharField(max_length=20)

