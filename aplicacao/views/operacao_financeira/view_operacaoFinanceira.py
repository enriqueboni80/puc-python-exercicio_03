from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Sum, Q
from ...models.operacaoFinanceira import (
    OperacaoFinanceira,
    OperacaoFinanceiraEntrada,
    OperacaoFinanceiraSaida,
)
from ...helpers.constantes import Constantes
from ...forms.rawOperacaoFinanceiraForm import RawPesquisarPorDataForm


def index(request):

    dataInicioDefault = "1900-01-01"
    dataFimDefault = "3000-12-31"
    dataInicio = dataInicioDefault
    dataFim = dataFimDefault


    formPesquisar = RawPesquisarPorDataForm(request.POST or None)

    if formPesquisar.is_valid():
        dataInicio = (
            formPesquisar.cleaned_data["data_inicio"]
            if formPesquisar.cleaned_data["data_inicio"] is not None
            else dataInicioDefault
        )
        dataFim = (
            formPesquisar.cleaned_data["data_fim"]
            if formPesquisar.cleaned_data["data_fim"] is not None
            else dataFimDefault
        )

    returnedObjects = OperacaoFinanceira.objects.getElementsOfAllSubClasses(
        dataInicio, dataFim
    )
    
    valorTotalEntradasRecebidas = OperacaoFinanceira.objects.getSomaRecebidos(dataInicio, dataFim)
    valorTotalEntradasAReceber = OperacaoFinanceira.objects.getSomaAReceber(dataInicio, dataFim)
    valorTotalSaidasPagas = OperacaoFinanceira.objects.getSomaPagas(dataInicio, dataFim)
    valorTotalSaidasAPagar = OperacaoFinanceira.objects.getSomaAPagar(dataInicio, dataFim)
    

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
