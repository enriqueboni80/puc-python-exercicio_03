from django.urls import path
from ..views import view_operacaoFinanceiraEntradas


urlpatterns = [
    path("", view_operacaoFinanceiraEntradas.index, name="operacao-financeira-entrada.index"),
    path("create/", view_operacaoFinanceiraEntradas.create, name="operacao-financeira-entrada.create"),
    path("store/", view_operacaoFinanceiraEntradas.store, name="operacao-financeira-entrada.store"),
    path("<int:id>/", view_operacaoFinanceiraEntradas.show, name="operacao-financeira-entrada.show"),
    path("<int:id>/edit", view_operacaoFinanceiraEntradas.edit, name="operacao-financeira-entrada.edit"),
    path("<int:id>/update", view_operacaoFinanceiraEntradas.update, name="operacao-financeira-entrada.update"),
    path("<int:id>/delete", view_operacaoFinanceiraEntradas.destroy, name="operacao-financeira-entrada.delete"),
]

