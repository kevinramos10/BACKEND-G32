from django.urls import path
from .views import UsuariosView

urlspatterns = [
    path('registro', UsuariosView.as_view())
]