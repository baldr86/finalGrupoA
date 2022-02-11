from django.urls import path
from app_biblioteca import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path("catalogo/", views.catalogo, name='catalogo'),
    path("listadocursos/", views.listadocursos, name='listadocursos'),
    path("buscarlibro/", views.buscarLibro, name="buscarlibro"),
    path("buscar/", views.buscar, name='buscar'),
    path("creatucuenta/", views.creatucuenta, name="creatucuenta"),
    path("accesoasocios/", views.accesoasocios, name='accesoasocios'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('accesoastaff/', views.accesoastaff, name='accesoastaff'),
  
    path('listaSocios/', views.SocioList.as_view(), name='List'),
    path('detalleSocios/<pk>/', views.SocioDetail.as_view(), name='Detail'),    
    path('crearSocios/', views.SocioCreate.as_view(), name='New'),   
    path('eliminaSocios/<pk>/', views.SocioDelete.as_view(), name='Delete'),  
    path('actualizaSocios/<pk>/', views.SocioUpdate.as_view(), name='Edit'),   

    path('listaLibros/', views.LibroList.as_view(), name='ListL'),
    path('detalleLibros/<pk>/', views.LibroDetail.as_view(), name='DetailL'),    
    path('crearLibros/', views.LibroCreate.as_view(), name='NewL'),   
    path('eliminaLibros/<pk>/', views.LibroDelete.as_view(), name='DeleteL'),  
    path('actualizaLibros/<pk>/', views.LibroUpdate.as_view(), name='EditL'),   

    path('listaCursos/', views.CursoList.as_view(), name='ListC'),
    path('detalleCursos/<pk>/', views.CursoDetail.as_view(), name='DetailC'),    
    path('crearCursos/', views.CursoCreate.as_view(), name='NewC'),   
    path('eliminaCursos/<pk>/', views.CursoDelete.as_view(), name='DeleteC'),  
    path('actualizaCursos/<pk>/', views.CursoUpdate.as_view(), name='EditC'),   

    path("postlist/", views.PostListView.as_view(), name = "postlist"),
    path("crearpost/", views.PostCreateView.as_view(), name = "crearpost"),
    path("<slug>/", views.PostDetailView.as_view(), name = "post_detail"),  
    path("<slug>/actualizarpost", views.PostUpdateView.as_view(), name = "actualizarpost"),
    path("<slug>/borrarpost", views.PostDeleteView.as_view(), name = "borrarpost"),

    path("like/<slug>/", views.like, name="like")


]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
