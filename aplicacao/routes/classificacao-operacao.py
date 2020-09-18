from django.urls import path
from ..views import view_classificacaoOperacoes


urlpatterns = [
    path("", view_classificacaoOperacoes.index, name="classificacao-operacao.index"),
    path("create/", view_classificacaoOperacoes.create, name="classificacao-operacao.create"),
    path("store/", view_classificacaoOperacoes.store, name="classificacao-operacao.store"),
    path("<int:id>/", view_classificacaoOperacoes.show, name="classificacao-operacao.show"),
    path("<int:id>/edit", view_classificacaoOperacoes.edit, name="classificacao-operacao.edit"),
    path("<int:id>/update", view_classificacaoOperacoes.update, name="classificacao-operacao.update"),
    path("<int:id>/delete", view_classificacaoOperacoes.destroy, name="classificacao-operacao.delete"),
]

