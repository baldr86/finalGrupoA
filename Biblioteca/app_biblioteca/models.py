from django.db import models
from django.shortcuts import reverse

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
        return f'Nombre y apellido: {self.nombre} - mail: {self.mail} - teléfono: {self.telefono} ' 

    nombre= models.CharField(max_length=40)
    documento= models.IntegerField()
    mail= models.EmailField()
    telefono= models.IntegerField()

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.TextField()
    imagen = models.ImageField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Socio, on_delete= models.CASCADE, default="")
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        
        return reverse("post_detail", kwargs={
            
            'slug': self.slug
            })
    def get_like_url(self):
        
        return reverse("like", kwargs={
            
            'slug': self.slug
            })


    @property
    def get_comment_count(self):
         return self.commented_posts.all().count()

    @property
    def get_view_count(self):
         return self.views_post.all().count()

    @property
    def get_like_count(self):
         return self.like_set.all().count()


class Comentarios(models.Model):
     usuario = models.ForeignKey(Socio, on_delete= models.CASCADE, default="")
     post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name="commented_posts")
     fechaComentario = models.DateTimeField(auto_now_add=True)
     contenido = models.TextField()

     def __str__(self):
        return self.usuario.username

     


class Vistas(models.Model):
    usuario = models.ForeignKey(Socio, on_delete= models.CASCADE, default="")
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name="views_post")
    fechaComentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.nombre  

class Like(models.Model):
    usuario = models.ForeignKey(Socio, on_delete= models.CASCADE, default="")
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
  

    def __str__(self):
        return self.usuario.nombre


