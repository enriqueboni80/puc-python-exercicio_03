from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ..models.classificacaoOperacao import ClassificacaoOperacao
from ..forms.rawClassificacaoOperacaoForm import RawClassificacaoOperacaoForm


def index(request):
    returnedObjects = ClassificacaoOperacao.objects.all().order_by('-id')
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "classificacao-operacao/listar.html", dados)


def create(request):
    form = RawClassificacaoOperacaoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "classificacao-operacao/create.html", dados)


def store(request):
    form = RawClassificacaoOperacaoForm(request.POST)
    if form.is_valid():
        ClassificacaoOperacao.objects.create(**form.cleaned_data)
        return redirect("classificacao-operacao.index")
    
    
def show(request, id):
    returnedObject = ClassificacaoOperacao.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "classificacao-operacao/detalhar.html", dados)


def edit(request, id):
    returnedObject = ClassificacaoOperacao.objects.filter(pk=id).values()[0]
    form = RawClassificacaoOperacaoForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "classificacao-operacao/edit.html", dados)


def update(request, id):
    returnedObject = ClassificacaoOperacao.objects.filter(pk=id)
    form = RawClassificacaoOperacaoForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(**form.cleaned_data)
        return redirect("classificacao-operacao.index")


def destroy(request, id):
    ClassificacaoOperacao.objects.get(pk=id).delete()
    return redirect("classificacao-operacao.index")
