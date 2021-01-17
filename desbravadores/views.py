from django.http import HttpResponse
from django.shortcuts import render, redirect
from .services import desbravador_service
from .entidades import desbravador
from .models import Desbravador
from .forms import DesbravadorForm

# Create your views here.

def listar_desbravadores(request):
    desbravadores = desbravador_service.listar_desbravadores()
    return render(request, 'desbravadores/lista_desbravadores.html', {'desbravadores': desbravadores})

def cadastrar_desbravador(request):
    if request.method == "POST":
        form = DesbravadorForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            sexo = form.cleaned_data["sexo"]
            data_nascimento = form.cleaned_data["data_nascimento"]
            email = form.cleaned_data["email"]
            desbravador_novo = desbravador.Desbravador(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                                       email=email)
            desbravador_service.cadastrar_desbravador(desbravador_novo)
            return redirect('listar_desbravadores')
    else:
        form = DesbravadorForm()
    return render(request, 'desbravadores/form_desbravador.html', {'form': form})

def listar_desbravador_id(request, id):
    desbravador = desbravador_service.listar_desbravador_id(id)
    return render(request, 'desbravadores/desbravacard.html', {'desbravador': desbravador})

def remover_desbravador(request, id):
    desbravador = desbravador_service.listar_desbravador_id(id)
    if request.method == "POST":
        desbravador_service.remover_desbravador(desbravador)
        return redirect('listar_desbravadores')
    return render(request, 'desbravadores/confirma_exclusao.html', {'desbravador': desbravador})

def editar_desbravador(request, id):
    desbravador_antigo = desbravador_service.listar_desbravador_id(id)
    form = DesbravadorForm(request.POST or None, instance=desbravador_antigo)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        email = form.cleaned_data["email"]
        desbravador_novo = desbravador.Desbravador(nome=nome,sexo=sexo, data_nascimento=data_nascimento,email=email)
        desbravador_service.editar_desbravador(desbravador_antigo,desbravador_novo)
        return redirect('listar_desbravadores')
    return render(request, 'desbravadores/form_desbravador.html', {'form': form})

