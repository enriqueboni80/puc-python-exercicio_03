from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models.tipoOperacao import TipoOperacao
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
    form = RawTipoOperacaoForm(request.POST)
    if form.is_valid():
        TipoOperacao.objects.create(**form.cleaned_data)
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
    form = RawTipoOperacaoForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(**form.cleaned_data)
        return redirect("tipo-operacao.index")
    
    
def destroy(request, id):
    TipoOperacao.objects.get(pk=id).delete()
    return redirect("tipo-operacao.index")
