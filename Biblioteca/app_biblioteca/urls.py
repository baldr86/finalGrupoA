from django.urls import path
#from app_biblioteca.models import Cursos
from app_biblioteca import views

urlpatterns = [
    path('', views.inicio),
    path("libros/", views.libros),
    path("cursos/", views.curso),
    
]
