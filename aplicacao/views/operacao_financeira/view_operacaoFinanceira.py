from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Sum
from ...models.operacaoFinanceira import (
    OperacaoFinanceira,
    OperacaoFinanceiraEntrada,
    OperacaoFinanceiraSaida,
)
from ...helpers.constantes import Constantes
from ...forms.rawOperacaoFinanceiraForm import RawPesquisarPorDataForm


def index(request):

    formPesquisar = RawPesquisarPorDataForm(request.POST or None)

    _dataInicio = "1900-01-01"
    _dataFim = "3000-12-31"

    if formPesquisar.is_valid():
        if formPesquisar.cleaned_data["data_inicio"] is not None:
            dataInicio = formPesquisar.cleaned_data["data_inicio"]
        else:
            dataInicio = _dataInicio
        
        if formPesquisar.cleaned_data["data_fim"] is not None:
            dataFim = formPesquisar.cleaned_data["data_fim"]
        else:
            dataFim = _dataFim
    

    returnedObjects = (
        OperacaoFinanceira.objects.select_subclasses().all().order_by("-id")
    )

    if OperacaoFinanceiraEntrada.objects.filter(situacao=Constantes.RECEBIDO).exists():
        valorTotalEntradasRecebidas = OperacaoFinanceiraEntrada.objects.filter(
            situacao=Constantes.RECEBIDO
        ).aggregate(Sum("valor"))["valor__sum"]
    else:
        valorTotalEntradasRecebidas = 0.0

    if OperacaoFinanceiraEntrada.objects.filter(situacao=Constantes.ARECEBER).exists():
        valorTotalEntradasAReceber = OperacaoFinanceiraEntrada.objects.filter(
            situacao=Constantes.ARECEBER
        ).aggregate(Sum("valor"))["valor__sum"]
    else:
        valorTotalEntradasAReceber = 0.0

    if OperacaoFinanceiraSaida.objects.filter(situacao=Constantes.PAGO).exists():
        valorTotalSaidasPagas = OperacaoFinanceiraSaida.objects.filter(
            situacao=Constantes.PAGO
        ).aggregate(Sum("valor"))["valor__sum"]
    else:
        valorTotalSaidasPagas = 0.0

    if OperacaoFinanceiraSaida.objects.filter(situacao=Constantes.APAGAR).exists():
        valorTotalSaidasAPagar = OperacaoFinanceiraSaida.objects.filter(
            situacao=Constantes.APAGAR
        ).aggregate(Sum("valor"))["valor__sum"]
    else:
        valorTotalSaidasAPagar = 0.0

    valorResultado = (
        valorTotalEntradasRecebidas
        + valorTotalEntradasAReceber
        - valorTotalSaidasPagas
        - valorTotalSaidasAPagar
    )

    dados = {
        "returnedObjectsList": returnedObjects,
        "valorResultado": valorResultado,
        "valorTotalEntradasRecebidas": valorTotalEntradasRecebidas,
        "valorTotalEntradasAReceber": valorTotalEntradasAReceber,
        "valorTotalSaidasPagas": valorTotalSaidasPagas,
        "valorTotalSaidasAPagar": valorTotalSaidasAPagar,
        "form": formPesquisar,
    }
    return render(request, "operacao-financeira/listar.html", dados)
