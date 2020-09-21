from django.urls import path
from ..views import view_tipoOperacao


urlpatterns = [
    path("", view_tipoOperacao.index, name="tipo-operacao.index"),
    path("create/", view_tipoOperacao.create, name="tipo-operacao.create"),
    path("store/", view_tipoOperacao.store, name="tipo-operacao.store"),
    path("<int:id>/", view_tipoOperacao.show, name="tipo-operacao.show"),
    path("<int:id>/edit", view_tipoOperacao.edit, name="tipo-operacao.edit"),
    path("<int:id>/update", view_tipoOperacao.update, name="tipo-operacao.update"),
    path("<int:id>/delete", view_tipoOperacao.destroy, name="tipo-operacao.delete"),
]

