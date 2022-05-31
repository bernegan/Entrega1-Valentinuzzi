from django.shortcuts import redirect, render
from app_foro.models import *
from django.db.models import Q




# Create your views here.

def Home(request):
    return render(request , 'home.html')

def Contacto(request):
    return render(request , 'contacto.html')

def Nosotros(request):
    return render(request , 'acerca_de_nosotros.html')

def Publicacion(request):
    return render(request , 'publicacion_foro.html')

def Busqueda(request):
    return render(request , 'busqueda.html')

def Sorteo(request):
    return render(request , 'sorteo.html')

def Formulario_publicacion(request):
    if request.method == "POST":
        Publicacion = publicacion(usuario = request.POST['usuario'] , tema_especifico = request.POST['tema_especifico'], consulta = request.POST['consulta'] )
        Publicacion.save()
        return render (request , 'publicacion_confirmada.html')
    
    return render (request, 'publicacion_foro.html')
    
def Formulario_contacto(request):
    if request.method == "POST":
        formulario_contacto = contacto(usuario = request.POST['usuario'] , email = request.POST['email'] , razon_contacto = request.POST['razon_contacto'] )
        formulario_contacto.save()
        return render(request , 'contacto_confirmado.html')
    
    return render(request,'contacto.html')
        
def Formulario_sorteo(request):
    if request.method == "POST":
        formulario_sorteo = sorteo(nombre = request.POST['nombre'] , apellido = request.POST['apellido'] , email = request.POST['email'] , telefono = request.POST['telefono'])
        formulario_sorteo.save()
        return render (request , 'sorteo_confirmado.html')
    
    return render(request , 'sorteo.html')

def Formulario_buscador(request):

    if request.GET["texto"]:
        buscador = request.GET["texto"]
        resultado = publicacion.objects.filter(Q(usuario__icontains = buscador) | Q(tema_especifico__icontains=buscador) | Q(consulta__icontains=buscador))
        
        return render(request , 'resultado_busqueda.html' , {'resultado':resultado})






 
        


