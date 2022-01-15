from django.urls import path
from app_biblioteca import views

urlpatterns = [
    path('', views.inicio),
    path("libros.html", views.libros)
    
]
