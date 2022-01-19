from django.urls import path
#from app_biblioteca.models import Cursos
from app_biblioteca import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path("libros/", views.libros, name='libros'),
    path("cursos/", views.cursos, name='cursos'),
    path("socios/", views.socios, name='socios'),
    path("catalogo/", views.catalogo, name='catalogo'),
    path("listadocursos/", views.listadocursos, name='listadocursos'),
    path("buscarlibro/", views.buscarLibro, name="buscarlibro"),
    path("buscar/", views.buscar, name='buscar'),
    path("creatucuenta/", views.creatucuenta, name="creatucuenta"),
    path("accesoasocios/", views.accesoasocios, name='accesoasocios'),
]
    

