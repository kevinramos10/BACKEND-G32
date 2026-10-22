from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls), para crear interfaz grafica por eso no va 
    path("", include("gestion.urls"))
]
