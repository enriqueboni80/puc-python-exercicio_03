from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from django.template import loader
from datetime import datetime
from ...models.operacaoFinanceira import OperacaoFinanceiraEntrada
from ...forms.rawOperacaoFinanceiraForm import RawOperacaoFinanceiraEntradaForm

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def index(request):
    returnedObjects = OperacaoFinanceiraEntrada.objects.all().order_by("-id")
    valorTotalEntradas = OperacaoFinanceiraEntrada.objects.all().aggregate(
        Sum("valor")
    )["valor__sum"]

    """ Converte valor para pt-br """
    for x in returnedObjects:
        x.valor = locale.currency(x.valor)

    dados = {
        "returnedObjectsList": returnedObjects,
        "valorResultado": locale.currency(valorTotalEntradas) if valorTotalEntradas is not None else 0.0,
    }
    return render(request, "operacao-financeira/entrada/listar.html", dados)


def create(request):
    form = RawOperacaoFinanceiraEntradaForm()
    dados = {"form": form}
    return render(request, "operacao-financeira/entrada/create.html", dados)


def store(request):
    form = RawOperacaoFinanceiraEntradaForm(request.POST)
    if form.is_valid():
        form.cleaned_data["valor"] = form.cleaned_data.get("valor").replace(",", ".")
        OperacaoFinanceiraEntrada.objects.create(**form.cleaned_data)
        return redirect("operacao-financeira-entrada.index")


def show(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.get(pk=id)
    returnedObject.valor = locale.currency(returnedObject.valor)
    dados = {"returnedObject": returnedObject}
    return render(request, "operacao-financeira/entrada/detalhar.html", dados)


def edit(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.filter(pk=id).values()[0]
    returnedObject["classificao_operacao"] = returnedObject.get(
        "classificao_operacao_id"
    )
    returnedObject["tipo_operacao"] = returnedObject.get("tipo_operacao_id")
    returnedObject["data_recebimento"] = (
        returnedObject["data_recebimento"].strftime("%d/%m/%Y")
        if returnedObject["data_recebimento"] is not None
        else None
    )
    returnedObject["data_previsao"] = (
        returnedObject["data_previsao"].strftime("%d/%m/%Y")
        if returnedObject["data_previsao"] is not None
        else None
    )
    returnedObject["valor"] = str(returnedObject.get("valor")).replace(".", ",")
    form = RawOperacaoFinanceiraEntradaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "operacao-financeira/entrada/edit.html", dados)


def update(request, id):
    returnedObject = OperacaoFinanceiraEntrada.objects.filter(pk=id)
    form = RawOperacaoFinanceiraEntradaForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data["valor"] = form.cleaned_data.get("valor").replace(",", ".")
        returnedObject.update(**form.cleaned_data)
        return redirect("operacao-financeira-entrada.index")


def destroy(request, id):
    OperacaoFinanceiraEntrada.objects.get(pk=id).delete()
    return redirect("operacao-financeira-entrada.index")
