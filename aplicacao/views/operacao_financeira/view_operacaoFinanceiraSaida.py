from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from ...models.operacaoFinanceira import OperacaoFinanceiraSaida
from ...forms.rawOperacaoFinanceiraForm import RawOperacaoFinanceiraSaidaForm


def index(request):
    returnedObjects = OperacaoFinanceiraSaida.objects.all().order_by('-id')
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "operacao-financeira/saida/listar.html", dados)


def create(request):
    form = RawOperacaoFinanceiraSaidaForm()
    dados = {"form": form}
    return render(request, "operacao-financeira/saida/create.html", dados)


def store(request):
    form = RawOperacaoFinanceiraSaidaForm(request.POST)
    if form.is_valid():
        OperacaoFinanceiraSaida.objects.create(**form.cleaned_data)
        return redirect("operacao-financeira-saida.index")


def show(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "operacao-financeira/saida/detalhar.html", dados)


def edit(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.filter(pk=id).values()[0]
    returnedObject['classificao_operacao'] = returnedObject.get('classificao_operacao_id')
    returnedObject['tipo_operacao'] = returnedObject.get('tipo_operacao_id')
    returnedObject['data_vencimento'] = returnedObject['data_vencimento'].strftime("%d/%m/%Y")
    returnedObject['data_pagamento'] = returnedObject['data_pagamento'].strftime("%d/%m/%Y")
    form = RawOperacaoFinanceiraSaidaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "operacao-financeira/saida/edit.html", dados)


def update(request, id):
    returnedObject = OperacaoFinanceiraSaida.objects.filter(pk=id)
    form = RawOperacaoFinanceiraSaidaForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(**form.cleaned_data)
        return redirect("operacao-financeira-saida.index")


def destroy(request, id):
    OperacaoFinanceiraSaida.objects.get(pk=id).delete()
    return redirect("operacao-financeira-saida.index")
