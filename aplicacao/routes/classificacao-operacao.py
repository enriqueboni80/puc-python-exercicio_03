from django.urls import path
from ..views import view_classificacaoOperacoes


urlpatterns = [
    path("classificacao-operacao", view_classificacaoOperacoes.index, name="classificacao-operacao.index"),
    path("classificacao-operacao/create/", view_classificacaoOperacoes.create, name="classificacao-operacao.create"),
    path("classificacao-operacao/store/", view_classificacaoOperacoes.store, name="classificacao-operacao.store"),
    path("classificacao-operacao/<int:id>/", view_classificacaoOperacoes.show, name="classificacao-operacao.show"),
    path("classificacao-operacao/<int:id>/edit", view_classificacaoOperacoes.edit, name="classificacao-operacao.edit"),
    path("classificacao-operacao/<int:id>/update", view_classificacaoOperacoes.update, name="classificacao-operacao.update"),
    path("classificacao-operacao/<int:id>/delete", view_classificacaoOperacoes.destroy, name="classificacao-operacao.delete"),
]

