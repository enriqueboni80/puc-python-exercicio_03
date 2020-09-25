from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from django.template import loader
from ...models.operacaoFinanceira import OperacaoFinanceiraSaida
from ...forms.rawOperacaoFinanceiraForm import RawOperacaoFinanceiraSaidaForm

import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def index(request):
    returnedObjects = OperacaoFinanceiraSaida.objects.all().order_by("-id")
    valorTotalSaidas = OperacaoFinanceiraSaida.objects.all().aggregate(Sum("valor"))[
        "valor__sum"
    ]

    """ Converte valor para pt-br """
    for x in returnedObjects:
        x.valor = locale.currency(x.valor)

    dados = {
        "returnedObjectsList": returnedObjects,
        "valorResultado": locale.currency(valorTotalSaidas) if valorTotalSaidas is not None else 0.0,
    }
    return render(request, "operacao-financeira/saida/listar.html", dados)


def create(request):
    form = RawOperacaoFinanceiraSaidaForm()
    dados = {"form": form}
    return render(request, "operacao-financeira/saida/create.html", dados)


def store(request):
    form = RawOperacaoFinanceiraSaidaForm(request.POST)
    if form.is_valid():
        form.cleaned_data["valor"] = form.cleaned_data.get("valor").replace(",", ".")
        OperacaoFinanceiraSaida.objects.create(**form.cleaned_data)
        return redirect("operacao-financeira-saida.index")


def show(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.get(pk=id)
    returnedObject.valor = locale.currency(returnedObject.valor)
    dados = {"returnedObject": returnedObject}
    return render(request, "operacao-financeira/saida/detalhar.html", dados)


def edit(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.filter(pk=id).values()[0]
    returnedObject["classificao_operacao"] = returnedObject.get(
        "classificao_operacao_id"
    )
    returnedObject["tipo_operacao"] = returnedObject.get("tipo_operacao_id")
    returnedObject["data_vencimento"] = (
        returnedObject["data_vencimento"].strftime("%d/%m/%Y")
        if returnedObject["data_vencimento"] is not None
        else None
    )
    returnedObject["data_pagamento"] = (
        returnedObject["data_pagamento"].strftime("%d/%m/%Y")
        if returnedObject["data_pagamento"] is not None
        else None
    )
    returnedObject["valor"] = str(returnedObject.get("valor")).replace(".", ",")
    form = RawOperacaoFinanceiraSaidaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "operacao-financeira/saida/edit.html", dados)


def update(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.filter(pk=id)
    form = RawOperacaoFinanceiraSaidaForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data["valor"] = form.cleaned_data.get("valor").replace(",", ".")
        returnedObject.update(**form.cleaned_data)
        return redirect("operacao-financeira-saida.index")


def destroy(request, id):
    OperacaoFinanceiraSaida.objects.get(pk=id).delete()
    return redirect("operacao-financeira-saida.index")
