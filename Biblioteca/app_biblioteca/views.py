from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from app_biblioteca.models import Libro
from app_biblioteca.forms import LibroFormulario
from app_biblioteca.models import Cursos

def inicio(request):

    return render(request, "inicio.html")


def libros(request):

      if request.method == 'POST':

            miFormulario = LibroFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  libro = Libro (nombre=informacion['nombre'], autor=informacion['autor'],
                  publicacion=informacion["publicacion"], genero=informacion["genero"],
                  editorial=informacion["editorial"] )

                  libro.save()

                  return render(request, "inicio.html") 

      else: 

            miFormulario= LibroFormulario()

      return render(request, "libros.html", {"miFormulario":miFormulario})

	


def curso(self):
      curso=Cursos(nombre=['nombre'], codigocurso=['codigocurso'], docente=['docente'], 
      diahorario= ['diahorario'] )

      curso.save()
      texto= f'Has creado el curso: {curso.nombre} comisión: {curso.codigocurso}'

      return HTTPResponse(texto)
