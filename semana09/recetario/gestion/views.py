from django.shortcuts import render
from .models import Receta

# Create your views here.

def listar_recetas(request):
    recetas = Receta.objects.all()
    return render(request, "lista_recetas.html", {"recetas": recetas})

