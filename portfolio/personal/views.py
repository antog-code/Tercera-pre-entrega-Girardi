from django.shortcuts import render
from .models import *

from .forms import*

#from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, "personal/index.html")

def index(request):
    return render(request, "personal/index.html")

def formacion(request):
    contexto = {"formacion": Estudios.objects.all(),}
    return render(request, "personal/formacion.html", contexto)

def experiencia(request):
    contexto = {"experiencia": Experiencia.objects.all()}
    return render(request, "personal/experiencia.html", contexto)

def proyectos(request):
    contexto = {"proyectos": Proyectos.objects.all()}
    return render(request, "personal/proyectos.html", contexto)

def coworking(request):
    contexto = {"coworking": ContactoCoworking.objects.all()}
    return render(request, "personal/coworking.html", contexto)

#def contacto(request):
#    contexto = {"contacto": Contacto.objects.all()}
#    return render(request, "personal/contacto.html", contexto)

def contacto_list(request):
    contexto = {"contacto_list": Contacto.objects.all()}
    return render(request, "personal/contacto_list.html", contexto)

def acerca(request):
    return render(request, "personal/acerca.html")


#___ Formularios
def contacto(request):
    if request.method == "POST":
        miForm = ContactoForm(request.POST)
        if miForm.is_valid():
            contacto_nombre = miForm.cleaned_data.get("nombre")
            contacto_email = miForm.cleaned_data.get("email")
            contacto_telefono = miForm.cleaned_data.get("telefono")
            contacto_mensaje = miForm.cleaned_data.get("mensaje")
            contacto = Contacto(nombre=contacto_nombre, email=contacto_email, telefono=contacto_telefono, mensaje=contacto_mensaje)
            contacto.save()
            contexto = {"contacto_list": Contacto.objects.all() }
            return render(request, "personal/contacto_list.html", contexto)
    else:
        miForm = ContactoForm()

    return render(request, "personal/contacto.html", {"form": miForm})


def estudioAgregar(request):
    if request.method == "POST":
        miForm = EstudiosForm(request.POST)
        if miForm.is_valid():
            estudio_titulo = miForm.cleaned_data.get("titulo")
            estudio_institucion = miForm.cleaned_data.get("institucion")
            estudio_fecha = miForm.cleaned_data.get("fecha")
            estudio_degree = miForm.cleaned_data.get("degree")
            estudio = Estudios(titulo=estudio_titulo, institucion=estudio_institucion, fecha=estudio_fecha, degree=estudio_degree)
            estudio.save()
            contexto = {"formacion": Estudios.objects.all(),}
            return render(request, "personal/formacion.html", contexto)
    else:
        miForm = EstudiosForm()

    return render(request, "personal/estudioAgregar.html", {"form": miForm})


def experienciaForm(request):
    if request.method == "POST":
        miForm = ExperienciaForm(request.POST)
        if miForm.is_valid():
            experiencia_nombre = miForm.cleaned_data.get("nombre")
            experiencia_inicio = miForm.cleaned_data.get("inicio")
            experiencia_fin = miForm.cleaned_data.get("fin")
            experiencia_empresa = miForm.cleaned_data.get("empresa")
            experiencia_descripcion = miForm.cleaned_data.get("descripcion")
            experiencia = Estudios(nombre=experiencia_nombre, inicio=experiencia_inicio, fin=experiencia_fin, empresa=experiencia_empresa, descripcion=experiencia_descripcion)
            experiencia.save()
            contexto = {"experiencia": Experiencia.objects.all()}
            return render(request, "personal/experiencia.html", contexto)
    else:
        miForm = ExperienciaForm()

    return render(request, "personal/experienciaForm.html", {"form": miForm})


def buscarContacto(request):
    return render(request, "personal/buscar.html")

def contactoEncontrar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        contacto = Contacto.objects.filter(nombre__icontains=patron)
        contexto = {'contacto': contacto}    
    else:
        contexto = {'contacto': Contacto.objects.all()}

    return render(request, "personal/contacto_list.html", contexto)