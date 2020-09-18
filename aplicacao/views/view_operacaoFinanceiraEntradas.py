from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.operacaoFinanceira import OperacaoFinanceiraEntrada
from django.template import loader

from ..forms import RawOperacaoFinanceiraEntradaForm


def index(request):
    returnedObjects = OperacaoFinanceiraEntrada.objects.all().order_by('-id')
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "operacao-financeira-entrada/listar.html", dados)


def create(request):
    form = RawOperacaoFinanceiraEntradaForm(request.POST or None)
    dados = {"form": form}
    return render(request, "operacao-financeira-entrada/create.html", dados)


def store(request):
    form = RawOperacaoFinanceiraEntradaForm(request.POST)
    if form.is_valid():
        OperacaoFinanceiraEntrada.objects.create(**form.cleaned_data)
        return redirect("operacao-financeira-entrada.index")


def show(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "operacao-financeira-entrada/detalhar.html", dados)


def edit(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.filter(pk=id).values()[0]
    form = RawOperacaoFinanceiraEntradaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "operacao-financeira-entrada/edit.html", dados)


def update(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.filter(pk=id)
    form = RawOperacaoFinanceiraEntradaForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(**form.cleaned_data)
        return redirect("operacao-financeira-entrada.index")


def destroy(request, id):
    OperacaoFinanceiraEntrada.objects.get(pk=id).delete()
    return redirect("classificacao-operacao.index")
