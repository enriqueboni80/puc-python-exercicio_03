from django.urls import path
from ..views.operacao_financeira import view_operacaoFinanceiraEntrada, view_operacaoFinanceiraSaida, view_operacaoFinanceira


urlpatterns = [
    path("", view_operacaoFinanceira.index, name="operacao-financeira.index"),
    path("entrada/", view_operacaoFinanceiraEntrada.index, name="operacao-financeira-entrada.index"),
    path("entrada/create/", view_operacaoFinanceiraEntrada.create, name="operacao-financeira-entrada.create"),
    path("entrada/store/", view_operacaoFinanceiraEntrada.store, name="operacao-financeira-entrada.store"),
    path("entrada/<int:id>/", view_operacaoFinanceiraEntrada.show, name="operacao-financeira-entrada.show"),
    path("entrada/<int:id>/edit", view_operacaoFinanceiraEntrada.edit, name="operacao-financeira-entrada.edit"),
    path("entrada/<int:id>/update", view_operacaoFinanceiraEntrada.update, name="operacao-financeira-entrada.update"),
    path("entrada/<int:id>/delete", view_operacaoFinanceiraEntrada.destroy, name="operacao-financeira-entrada.delete"),
    path("saida/", view_operacaoFinanceiraSaida.index, name="operacao-financeira-saida.index"),
    path("saida/create/", view_operacaoFinanceiraSaida.create, name="operacao-financeira-saida.create"),
    path("saida/store/", view_operacaoFinanceiraSaida.store, name="operacao-financeira-saida.store"),
    path("saida/<int:id>/", view_operacaoFinanceiraSaida.show, name="operacao-financeira-saida.show"),
    path("saida/<int:id>/edit", view_operacaoFinanceiraSaida.edit, name="operacao-financeira-saida.edit"),
    path("saida/<int:id>/update", view_operacaoFinanceiraSaida.update, name="operacao-financeira-saida.update"),
    path("saida/<int:id>/delete", view_operacaoFinanceiraSaida.destroy, name="operacao-financeira-saida.delete"),
]

