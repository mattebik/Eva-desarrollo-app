from django.http import HttpResponse
from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'base.html')

def pagina_formulario(request):
    return render(request, 'formulario.html')

def bienvenida(request):
    return HttpResponse("Bienvenid@")

def pagina_menu(request):
    return render(request, 'menu.html')