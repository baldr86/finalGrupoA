from django.urls import path
from ProyectoGrupoA.finalGrupoA.Biblioteca.app_biblioteca.models import Cursos
from ProyectoGrupoA.finalGrupoA.Biblioteca.app_biblioteca.views import curso
from app_biblioteca import views

urlpatterns = [
    path('', views.inicio),
    path("libros.html", views.libros),
    path("cursos.html", views.curso)
]
