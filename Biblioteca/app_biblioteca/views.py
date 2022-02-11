from dataclasses import field
from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app_biblioteca.forms import LibroFormulario, SocioFormulario, CursoFormulario, UserRegisterForm, postForm, CommentForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.admin.views.decorators import staff_member_required
#from django.contrib.auth.decorators import user_passes_test
from app_biblioteca.models import Curso, Like, Post, Socio, Libro, Vistas
from django.db.models.functions import Lower, Replace
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def inicio(request):

    return render(request, "inicio.html")


def catalogo(request):

    catalogo = Libro.objects.all()

    return render (request, 'catalogo.html', {'catalogo':catalogo} )


def listadocursos (request):

    listacurso = Curso.objects.all()

    return render (request, 'listadocursos.html', {'listacurso':listacurso} )  


def buscarLibro (request):

      return render(request, 'buscarlibro.html')


def buscar(request):
      if request.method == "GET":

            libro = request.GET["libro"].lower()
            libros= Libro.objects.filter(nombre__icontains=libro)

            return render(request, "resultado.html",{"libro": libro, "libros": libros})
     

      else: 
           respuesta=  "No se encuentra el libro"

      return HttpResponse(respuesta)

def creatucuenta (request):

    if request.method == "POST":

        #form = UserCreationForm (request.POST)
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            #form.cleaned_data ['groups'] = 'Asociados'
            form.save()
            #form.cleaned_data ['groups'] = 'Asociados'
            print (form)
            return render (request, 'padre.html', {'mensaje': 'Usuario Creado con éxito :) '})
           
        else:
            return render (request, 'padre.html', {'mensaje': 'Usuario no creado, intenta nuevamente'})

    else:
        #form = UserCreationForm ()
        form = UserRegisterForm ()
        return render (request, 'creatucuenta.html', {'form': form})

def accesoasocios (request):

    if request.method == "POST":
        form = AuthenticationForm (request, data=request.POST)
        if form.is_valid():

            data= form.cleaned_data
            user = authenticate (username=data['username'], password=data['password'])

            if user is not None:

                login (request, user)
                return render (request, 'padre.html')
              
            else:

                return render (request, "padre.html", {"mensaje": "Falló la autenticación"})

        else:
            return render (request, "padre.html", {"mensaje": "Ingreso erróneo, intenta nuevamente"})
        
    else:
        form = AuthenticationForm()
        return render (request, "accesoasocios.html", {'form': form})

def accesoastaff (request):
    
    return render (request, 'menustaff.html')
              

class SocioList (LoginRequiredMixin, ListView):

    model = Socio
    template_name= "socio_list.html"

class SocioDetail (DetailView):

    model = Socio
    template_name= "socio_detail.html"

class SocioUpdate (UpdateView):

    model = Socio
    success_url= '/app_biblioteca/listaSocios'
    fields = ['nombre', 'documento', 'mail', 'telefono']
    template_name= 'socio_form.html'
   
    
class SocioCreate (CreateView):

    model = Socio
    success_url= '/app_biblioteca/listaSocios'
    fields = ['nombre', 'documento', 'mail', 'telefono']    
    template_name= 'socios.html'
    

class SocioDelete (DeleteView):

    model = Socio
    success_url= '/app_biblioteca/listaSocios'
    template_name= 'socio_confirm_delete.html'

  
class LibroList (LoginRequiredMixin, ListView):

    model = Libro
    template_name= "libro_list.html"

class LibroDetail (DetailView):

    model = Libro
    template_name= "libro_detail.html"

class LibroUpdate (UpdateView):

    model = Libro
    success_url= '/app_biblioteca/listaLibros'
    fields = ['nombre', 'autor', 'publicacion', 'genero', 'editorial']
    template_name= 'libro_form.html'
       
class LibroCreate (CreateView):

    model = Libro
    success_url= '/app_biblioteca/listaLibros'
    fields = ['nombre', 'autor', 'publicacion', 'genero', 'editorial']   
    template_name= 'libros.html'
    
class LibroDelete (DeleteView):

    model = Libro
    success_url= '/app_biblioteca/listaLibros'
    template_name= 'libro_confirm_delete.html'

  
class CursoList (LoginRequiredMixin, ListView):

    model = Curso
    template_name= "curso_list.html"

class CursoDetail (DetailView):

    model = Curso
    template_name= "curso_detail.html"

class CursoUpdate (UpdateView):

    model = Curso
    success_url= '/app_biblioteca/listaCursos'
    fields = ['nombre', 'codigocurso', 'docente', 'diahorario']
    template_name= 'curso_form.html'
       
class CursoCreate (CreateView):

    model = Curso
    success_url= '/app_biblioteca/listaCursos'
    fields = ['nombre', 'codigocurso', 'docente', 'diahorario']   
    template_name= 'cursos.html'
    
class CursoDelete (DeleteView):

    model = Curso
    success_url= '/app_biblioteca/listaCursos'
    template_name= 'curso_confirm_delete.html'


#POST DE SOCIOS

class PostListView (ListView):

    model = Post
    template_name= "post_list.html"

class PostDetailView (DetailView):

    model = Post
    template_name= "post_detail.html"
    
    def post (self, *args,**kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.usuario = self.request.user
            comment.post = post
            comment.save()
            
            return redirect("post_detail", slug=self.get_object().slug)
        return redirect("post_detail", slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({ "form" : CommentForm()})
        return context



    def get_object(self, **kwargs):
        
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            Vistas.objects.get_or_create(user= self.request.user, post=object)
        return object

class PostCreateView (CreateView):
    form_class = postForm
    model = Post

    template_name= 'post_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Crear',
        })
        return context
        
    success_url= '/postlist'

class PostUpdateView (UpdateView):
    form_class = postForm
    model = Post

    template_name= 'post_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Actualizar'
        })
        return context

    success_url= '/postlist'    

class PostDeleteView (DeleteView):

    model = Post
    template_name= 'post_confirm_delete.html'
    success_url= '/postlist'

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(usuario=request.user, post=post)

    if like_qs.exists():
        like_qs[0].delete()

        return redirect("post_detail", slug=slug)

    Like.objects.create(usuario=request.user, post=post)

    return redirect("post_detail", slug=slug)