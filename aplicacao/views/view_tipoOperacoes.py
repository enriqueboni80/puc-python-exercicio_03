from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.tipoOperacao import TipoOperacao
from django.template import loader

from ..forms.rawTipoOperacaoForm import RawTipoOperacaoForm


def index(request):
    returnedObjects = TipoOperacao.objects.all().order_by('-id')
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "tipo-operacao/listar.html", dados)


def create(request):
    form = RawTipoOperacaoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "tipo-operacao/create.html", dados)


def store(request):
    if request.method == "POST":
        tipoOperacao = TipoOperacao(
            nome=request.POST["nome"], descricao=request.POST["descricao"],
        )
        tipoOperacao.save()
        return redirect("tipo-operacao.index")


def show(request, id):
    returnedObject = TipoOperacao.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "tipo-operacao/detalhar.html", dados)


def edit(request, id):
    returnedObject = TipoOperacao.objects.get(pk=id)
    form = RawTipoOperacaoForm({"nome": returnedObject.nome, "descricao": returnedObject.descricao})
    dados = {"returnedObject_id": returnedObject.id, "form": form}
    return render(request, "tipo-operacao/edit.html", dados)


def update(request, id):
    returnedObject = TipoOperacao.objects.filter(pk=id)
    returnedObject.update(
        nome=request.POST["nome"], descricao=request.POST["descricao"],
    )
    return redirect("tipo-operacao.index")


def destroy(request, id):
    TipoOperacao.objects.get(pk=id).delete()
    return redirect("tipo-operacao.index")
