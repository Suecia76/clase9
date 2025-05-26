from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    return HttpResponse("¡Hola, mundo!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1 style='color:red;'>¡Hola, mundo!</h1>")

def saludar_con_parametros(request, nombre:str,apellido:str):
    return HttpResponse(f"<h1 style='color:blue;'>¡Hola, {nombre} {apellido}!</h1>")

def index(request):
    return render(request, 'core/index.html')