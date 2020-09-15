from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.pessoa import Pessoa
from ..models.departamento import Departamento
from django.template import loader

from ..forms import RawPessoaForm


""" return HttpResponse("Chegou aqui") """


def index(request):
    lista_p = Pessoa.objects.all()
    dados = {
        "listaPessoas": lista_p,
    }
    return render(request, "pessoa/listar.html", dados)


def create(request):
    lista_depto = Departamento.objects.all()
    form = RawPessoaForm(request.POST or None)
    dados = {
        "form": form,
    }
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


def show(request, idPessoa):
    p = Pessoa.objects.get(pk=idPessoa)
    dados = {"pessoa": p}
    return render(request, "pessoa/detalhar.html", dados)


def edit(request, idPessoa):
    pessoa = Pessoa.objects.get(pk=idPessoa)
    form = RawPessoaForm(
        {
            "nome": pessoa.nome,
            "sobrenome": pessoa.sobrenome,
            "idade": pessoa.idade,
            "depto_atual": pessoa.depto_atual,
            "depto_chefia": pessoa.depto_chefia,
            "escolaridade": pessoa.escolaridade,
        }
    )
    dados = {"pessoa_id": pessoa.id, "form": form}
    return render(request, "pessoa/edit.html", dados)


def update(request, idPessoa):
    pessoa = Pessoa.objects.filter(pk=idPessoa)
    pessoa.update(
        nome=request.POST["nome"],
        sobrenome=request.POST["sobrenome"],
        idade=request.POST["idade"],
        depto_atual_id=request.POST["depto_atual"],
        depto_chefia_id=request.POST["depto_chefia"],
        escolaridade=request.POST["escolaridade"],
    )
    return redirect("pessoa.index")


def destroy(request, idPessoa):
    Pessoa.objects.get(pk=idPessoa).delete()
    return redirect("pessoa.index")
