from django.urls import path
from .views import *


urlpatterns = [
    path('listar', listar_desbravadores, name='listar_desbravadores'),
    path('cadastrar', cadastrar_desbravador, name='cadastrar_desbravador'),
    path('listar/<int:id>', listar_desbravador_id, name='listar_desbravador_id'),
    path('editar/<int:id>', editar_desbravador, name='editar_desbravador'),
    path('remover/<int:id>', remover_desbravador, name='remover_desbravador')
]