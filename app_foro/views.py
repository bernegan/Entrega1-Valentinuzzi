from django.shortcuts import  render
from app_foro.models import *
from django.db.models import Q
from app_foro.forms import Sorteo_formulario,Publicacion_formulario, Contacto_formulario
from datetime import datetime




# Create your views here.

def Home(request):
    return render(request , 'home.html')

def Contacto(request):
    return render(request , 'contacto/contacto.html')

def Nosotros(request):
    return render(request , 'acerca_de_nosotros.html')

def Publicacion(request):
    return render(request , 'publicacion/publicacion_foro.html')

def Busqueda(request):
    return render(request , 'busqueda/busqueda.html')

def Sorteo(request):
    return render(request , 'sorteo/sorteo.html')

def Formulario_publicacion(request):
    if request.method == "POST":
        
        formulario_publicaion = Publicacion_formulario(request.POST)
        if formulario_publicaion.is_valid():
            datos = formulario_publicaion.cleaned_data

            datos_publicacion = publicacion(usuario = datos['usuario'] , tema_especifico = datos['tema_especifico'] , consulta = datos['consulta'] , fecha_de_publicacion = datetime.now())
            datos_publicacion.save()
            return render (request , 'publicacion/publicacion_confirmada.html')
        
        else:
            return render (request , 'publicacion/publicacion_rechazada.html')
            
       
    return render (request, 'publicacion/publicacion_foro.html')
       
def Formulario_contacto(request):
    if request.method == "POST":
        
        formulario_contacto = Contacto_formulario(request.POST)
        if formulario_contacto.is_valid():
            
            datos = formulario_contacto.cleaned_data

            datos_contactante = contacto(usuario = datos['usuario'] , email = datos['email'] , razon_contacto = datos['razon_contacto'] , fecha_de_contacto = datetime.now() )
            datos_contactante.save()
            return render(request , 'contacto/contacto_confirmado.html')
        
        else:
            return render(request , 'contacto/rechazo_contacto.html')
    
    return render(request,'contacto/contacto.html')

def Formulario_sorteo(request):
    if request.method == "POST":

        formulario_sorteo = Sorteo_formulario(request.POST)
        if formulario_sorteo.is_valid():
            
            datos = formulario_sorteo.cleaned_data

            datos_sorteo = sorteo(nombre = datos['nombre'] , apellido = datos['apellido'] , email = datos['email'] , telefono = datos['telefono'])
            datos_sorteo.save()
            return render (request , 'sorteo/sorteo_confirmado.html')
        else:
            return render(request, 'sorteo/rechazo_sorteo.html')


        
            
    return render(request , 'sorteo/sorteo.html')

def Formulario_buscador(request):

    if request.GET["texto"]:
        buscador = request.GET["texto"]
        resultado = publicacion.objects.filter(Q(usuario__icontains = buscador) | Q(tema_especifico__icontains=buscador) | Q(consulta__icontains=buscador))
        
        return render(request , 'busqueda/resultado_busqueda.html' , {'resultado':resultado})






 
        


