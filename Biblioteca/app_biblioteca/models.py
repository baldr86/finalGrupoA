from django.db import models

class Libro(models.Model):

    def __str__(self):
        return f'Título: {self.nombre} - autor: {self.autor} - género: {self.genero}' 

    nombre= models.CharField(max_length=40)
    autor= models.CharField(max_length=30)
    publicacion= models.IntegerField()
    genero= models.CharField(max_length=20)
    editorial=models.CharField(max_length=20)

class Curso(models.Model):

    def __str__(self):
        return f'Nombre: {self.nombre} - Dia y hora: {self.diahorario}' 

    nombre=models.CharField(max_length=40)
    codigocurso=models.IntegerField()
    docente=models.CharField(max_length=30)
    diahorario=models.CharField(max_length=40)

class Socio(models.Model):

    def __str__(self):
        return f'Nombre y apellido: {self.nombre} - mail: {self.mail} - teléfono: {self.telefono}' 

    nombre= models.CharField(max_length=40)
    documento= models.IntegerField()
    mail= models.EmailField()
    telefono= models.IntegerField()

