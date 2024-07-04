from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=12, required=True)
    mensaje = forms.CharField(max_length=300)

class EstudiosForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    institucion = forms.CharField(max_length=50, required=True)
    anio = forms.CharField(max_length=10, required=True)
    degree = forms.CharField(max_length=20, required=True)


class ExperienciaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    inicio = forms.CharField(max_length=10)
    fin = forms.CharField(max_length=10)
    empresa = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=300)

