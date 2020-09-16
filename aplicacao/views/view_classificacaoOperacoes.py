from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.classificacaoOperacao import ClassificacaoOperacao
from django.template import loader

from ..forms import RawClassificacaoOperacaoForm


def index(request):
    returnedObjects = ClassificacaoOperacao.objects.all()
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "classificacao-operacao/listar.html", dados)


def create(request):
    form = RawClassificacaoOperacaoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "classificacao-operacao/create.html", dados)


def store(request):
    if request.method == "POST":
        classificacaoOperacao = ClassificacaoOperacao(
            nome=request.POST["nome"], descricao=request.POST["descricao"],
        )
        classificacaoOperacao.save()
        return redirect("classificacao-operacao.index")


def show(request, id):
    returnedObject = ClassificacaoOperacao.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "classificacao-operacao/detalhar.html", dados)


def edit(request, id):
    returnedObject = ClassificacaoOperacao.objects.get(pk=id)
    form = RawClassificacaoOperacaoForm({"nome": returnedObject.nome, "descricao": returnedObject.descricao})
    dados = {"returnedObject_id": returnedObject.id, "form": form}
    return render(request, "classificacao-operacao/edit.html", dados)


def update(request, id):
    returnedObject = ClassificacaoOperacao.objects.filter(pk=id)
    returnedObject.update(
        nome=request.POST["nome"], descricao=request.POST["descricao"],
    )
    return redirect("classificacao-operacao.index")


def destroy(request, id):
    ClassificacaoOperacao.objects.get(pk=id).delete()
    return redirect("classificacao-operacao.index")
