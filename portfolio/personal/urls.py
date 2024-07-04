from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('index/', index, name="index"),
    path('proyectos/', proyectos, name="proyectos"),
    path('experiencia/', experiencia, name="experiencia"),
    path('formacion/', formacion, name="formacion"),
    
    path('contacto_list/', contacto_list, name="contacto_list"),

    path('acerca/', acerca, name="acerca"),

    #----Formularios
    path('contacto/', contacto, name="contacto"),
    path('estudioAgregar/', estudioAgregar, name="estudioAgregar"),
    path('experienciaForm/', experienciaForm, name="experienciaForm"),

    path('buscar/', buscarContacto, name="buscar"),
    path('contactoEncontrar/', contactoEncontrar, name="contactoEncontrar"),

]
