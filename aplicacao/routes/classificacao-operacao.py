from django.urls import path
from ..views import view_classificacaoOperacao


urlpatterns = [
    path("", view_classificacaoOperacao.index, name="classificacao-operacao.index"),
    path("create/", view_classificacaoOperacao.create, name="classificacao-operacao.create"),
    path("store/", view_classificacaoOperacao.store, name="classificacao-operacao.store"),
    path("<int:id>/", view_classificacaoOperacao.show, name="classificacao-operacao.show"),
    path("<int:id>/edit", view_classificacaoOperacao.edit, name="classificacao-operacao.edit"),
    path("<int:id>/update", view_classificacaoOperacao.update, name="classificacao-operacao.update"),
    path("<int:id>/delete", view_classificacaoOperacao.destroy, name="classificacao-operacao.delete"),
]

