from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.pessoa import Pessoa
from ..models.departamento import Departamento
from django.template import loader

from ..forms import RawPessoaForm


""" return HttpResponse("Chegou aqui") """


def index(request):
    returnedObjects = Pessoa.objects.all()
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "pessoa/listar.html", dados)


def create(request):
    form = RawPessoaForm(request.POST or None)
    dados = {"form": form, "qtdDepartamentos": Departamento.objects.count()}
    return render(request, "pessoa/create.html", dados)


def store(request):
    pessoa = Pessoa(
        nome=request.POST["nome"],
        sobrenome=request.POST["sobrenome"],
        idade=request.POST["idade"],
        depto_atual_id=request.POST["depto_atual"],
        depto_chefia_id=request.POST["depto_chefia"],
        escolaridade=request.POST["escolaridade"],
    )
    pessoa.save()
    return redirect("pessoa.index")


def show(request, id):
    returnedObject = Pessoa.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "pessoa/detalhar.html", dados)


def edit(request, id):
    returnedObject = Pessoa.objects.filter(pk=id).values()[0]
    form = RawPessoaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "pessoa/edit.html", dados)


def update(request, id):
    pessoa = Pessoa.objects.filter(pk=id)
    pessoa.update(
        nome=request.POST["nome"],
        sobrenome=request.POST["sobrenome"],
        idade=request.POST["idade"],
        depto_atual_id=request.POST["depto_atual"],
        depto_chefia_id=request.POST["depto_chefia"],
        escolaridade=request.POST["escolaridade"],
    )
    return redirect("pessoa.index")


def destroy(request, id):
    Pessoa.objects.get(pk=idPessoa).delete()
    return redirect("pessoa.index")
