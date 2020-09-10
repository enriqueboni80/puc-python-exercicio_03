from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.pessoa import Pessoa
from django.template import loader


""" return HttpResponse("Chegou aqui") """

def index(request):

    lista_p = Pessoa.objects.all()
    dados = {"listapessoas": lista_p}
    return render(request, "pessoa/listar.html", dados)


def create(request):
    dados = {"form_action": "pessoa.store"}
    return render(request, "pessoa/form.html", dados)


def store(request):
    if request.method == "POST":
        pessoa = Pessoa(
            nome=request.POST["nome"],
            sobrenome=request.POST["sobrenome"],
            idade=request.POST["idade"],
            depto_atual_id=request.POST["depto_atual"],
            depto_chefia_id=None,
            escolaridade=request.POST["escolaridade"],
        )
        pessoa.save()
        return redirect("index")


def show(request, idPessoa):
    p = Pessoa.objects.get(pk=idPessoa)
    dados = {"pessoa": p}
    return render(request, "pessoa/detalhar.html", dados)


def edit(request, idPessoa):
    p = Pessoa.objects.get(pk=idPessoa)
    dados = {"pessoa": p, "form_action": "pessoa.update"}
    return render(request, "pessoa/form.html", dados)


def update(request):
    idPessoa = request.POST["_pessoa_id"]
    pessoa = Pessoa.objects.filter(pk=idPessoa)
    pessoa.update(
        nome=request.POST["nome"],
        sobrenome=request.POST["sobrenome"],
        idade=request.POST["idade"],
        depto_atual_id=request.POST["depto_atual"],
        depto_chefia_id=None,
        escolaridade=request.POST["escolaridade"],
    )
    return redirect("index")


def destroy(request, idPessoa):
    Pessoa.objects.get(pk=idPessoa).delete()
    return redirect("index")