from django.urls import path
from ..views import view_tipoOperacoes


urlpatterns = [
    path("tipo-operacao", view_tipoOperacoes.index, name="tipo-operacao.index"),
    path("tipo-operacao/create/", view_tipoOperacoes.create, name="tipo-operacao.create"),
    path("tipo-operacao/store/", view_tipoOperacoes.store, name="tipo-operacao.store"),
    path("tipo-operacao/<int:id>/", view_tipoOperacoes.show, name="tipo-operacao.show"),
    path("tipo-operacao/<int:id>/edit", view_tipoOperacoes.edit, name="tipo-operacao.edit"),
    path("tipo-operacao/<int:id>/update", view_tipoOperacoes.update, name="tipo-operacao.update"),
    path("tipo-operacao/<int:id>/delete", view_tipoOperacoes.destroy, name="tipo-operacao.delete"),
]

