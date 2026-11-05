from django.urls import path
from .views import listar_recetas

#Si la variable no se llama urlpatterns django no la encontrara y no podran ser accedidas
urlpatterns = [
    path("recetas/", listar_recetas),
]