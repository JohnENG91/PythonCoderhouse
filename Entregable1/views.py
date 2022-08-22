from django.shortcuts import render
from Entregable1.models import modelo_familiares
import datetime

# Create your views here.

def datos_hermano(request):
    familiar1 = modelo_familiares(
        nombre = "Pedro", 
        apellido = "Benitez", 
        parentesco = "hermano", 
        edad = 32, 
        celular = 1144556677,
        horario_consulta = datetime.datetime.now()
        )
    familiar1.save()
    contexto = {'datos_hermano' : familiar1}
    
    return render(request, 'template_hermanos.html', contexto)

def datos_primo(request):
    familiar2 = modelo_familiares(
        nombre = "Fabricio", 
        apellido = "Quiroga", 
        parentesco = "primo", 
        edad = 24, 
        celular = 1144452347,
        horario_consulta = datetime.datetime.now()
        )
    familiar2.save()
    contexto2 = {'datos_primo' : familiar2}
    
    return render(request, 'template_primos.html', contexto2)

def datos_tio(request):
    familiar3 = modelo_familiares(
        nombre = "Claudio", 
        apellido = "Quiroga", 
        parentesco = "tio", 
        edad = 64, 
        celular = 1144226577,
        horario_consulta = datetime.datetime.now()
        )
    familiar3.save()
    contexto3 = {'datos_tio' : familiar3}
    
    return render(request, 'template_tios.html', contexto3)