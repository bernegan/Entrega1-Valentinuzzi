from django.urls import path
from app_foro import views

urlpatterns = [
    path('' , views.Home),
    path('home' , views.Home , name= 'home'),
    path('contacto' , views.Contacto , name= 'contacto'),
    path('nosotros' , views.Nosotros , name= 'nosotros'),
    path('publicacion' , views.Publicacion , name= 'publicacion'),
    path('busqueda' , views.Busqueda , name= 'busqueda'),
    path('sorteo' , views.Sorteo , name= 'sorteo'),
    path('formulario_buscador' , views.Formulario_buscador),
    path('formulario_publicacion' , views.Formulario_publicacion , name= 'formulario_publicacion'),
    path('formulario_sorteo' , views.Formulario_sorteo , name='formulario_sorteo'),
    path('formulario_contacto' , views.Formulario_contacto , name='formulario_contacto'),
    


] 