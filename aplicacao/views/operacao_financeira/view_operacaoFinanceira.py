from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ...models.operacaoFinanceira import OperacaoFinanceira
from django.template import loader

from ...forms.rawOperacaoFinanceiraForm import RawOperacaoFinanceiraEntradaForm


def index(request):
    returnedObjects = (
        OperacaoFinanceira.objects.select_subclasses(
            "operacaofinanceiraentrada", "operacaofinanceirasaida"
        )
        .all()
        .order_by("-id")
    )
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "operacao-financeira/listar.html", dados)
