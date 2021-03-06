from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models.pessoa import Pessoa
from ..models.departamento import Departamento


def index(request):
    lista_pessoas = Pessoa.objects.all().order_by('-id')
    lista_departamentos = Departamento.objects.all().order_by('-id')
    dados = {
        "listaPessoas": lista_pessoas,
        "listaDepartamentos": lista_departamentos
    }
    return render(request, "home/index.html", dados)

