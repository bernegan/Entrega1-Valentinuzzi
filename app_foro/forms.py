from django import forms



class Publicacion_formulario(forms.Form):
    usuario = forms.CharField(max_length=40)
    tema_especifico = forms.CharField(max_length=40)
    consulta = forms.CharField(widget=forms.Textarea)
    

class Contacto_formulario(forms.Form):
    usuario = forms.CharField(max_length=40)
    email = forms.EmailField()
    razon_contacto = forms.CharField(widget=forms.Textarea)
    

class Sorteo_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()

