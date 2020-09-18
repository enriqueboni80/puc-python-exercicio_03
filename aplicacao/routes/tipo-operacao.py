from django.urls import path
from ..views import view_tipoOperacoes


urlpatterns = [
    path("", view_tipoOperacoes.index, name="tipo-operacao.index"),
    path("create/", view_tipoOperacoes.create, name="tipo-operacao.create"),
    path("store/", view_tipoOperacoes.store, name="tipo-operacao.store"),
    path("<int:id>/", view_tipoOperacoes.show, name="tipo-operacao.show"),
    path("<int:id>/edit", view_tipoOperacoes.edit, name="tipo-operacao.edit"),
    path("<int:id>/update", view_tipoOperacoes.update, name="tipo-operacao.update"),
    path("<int:id>/delete", view_tipoOperacoes.destroy, name="tipo-operacao.delete"),
]

