from django.urls import path
from .views import buscar_ruta

urlpatterns = [
    path('buscar-ruta/', buscar_ruta),
]