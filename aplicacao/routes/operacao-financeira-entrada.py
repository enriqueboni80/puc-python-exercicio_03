from django.urls import path
from ..views import view_operacaoFinanceiraEntradas


urlpatterns = [
    path("operacao-financeira-entrada", view_operacaoFinanceiraEntradas.index, name="operacao-financeira-entrada.index"),
    path("operacao-financeira-entrada/create/", view_operacaoFinanceiraEntradas.create, name="operacao-financeira-entrada.create"),
    path("operacao-financeira-entrada/store/", view_operacaoFinanceiraEntradas.store, name="operacao-financeira-entrada.store"),
    path("operacao-financeira-entrada/<int:id>/", view_operacaoFinanceiraEntradas.show, name="operacao-financeira-entrada.show"),
    path("operacao-financeira-entrada/<int:id>/edit", view_operacaoFinanceiraEntradas.edit, name="operacao-financeira-entrada.edit"),
    path("operacao-financeira-entrada/<int:id>/update", view_operacaoFinanceiraEntradas.update, name="operacao-financeira-entrada.update"),
    path("operacao-financeira-entrada/<int:id>/delete", view_operacaoFinanceiraEntradas.destroy, name="operacao-financeira-entrada.delete"),
]

