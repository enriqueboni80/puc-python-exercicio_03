from django.urls import path
from ..views.operacao_financeira import view_operacaoFinanceiraEntrada


urlpatterns = [
    path("entrada/", view_operacaoFinanceiraEntrada.index, name="operacao-financeira-entrada.index"),
    path("entrada/create/", view_operacaoFinanceiraEntrada.create, name="operacao-financeira-entrada.create"),
    path("entrada/store/", view_operacaoFinanceiraEntrada.store, name="operacao-financeira-entrada.store"),
    path("entrada/<int:id>/", view_operacaoFinanceiraEntrada.show, name="operacao-financeira-entrada.show"),
    path("entrada/<int:id>/edit", view_operacaoFinanceiraEntrada.edit, name="operacao-financeira-entrada.edit"),
    path("entrada/<int:id>/update", view_operacaoFinanceiraEntrada.update, name="operacao-financeira-entrada.update"),
    path("entrada/<int:id>/delete", view_operacaoFinanceiraEntrada.destroy, name="operacao-financeira-entrada.delete"),
]

