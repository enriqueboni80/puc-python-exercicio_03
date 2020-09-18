from django.urls import path
from ..views import view_pessoas


urlpatterns = [
    path("pessoa", view_pessoas.index, name="pessoa.index"),
    path("pessoa/create/", view_pessoas.create, name="pessoa.create"),
    path("pessoa/store/", view_pessoas.store, name="pessoa.store"),
    path("pessoa/<int:id>/", view_pessoas.show, name="pessoa.show"),
    path("pessoa/<int:id>/edit", view_pessoas.edit, name="pessoa.edit"),
    path("pessoa/<int:id>/update", view_pessoas.update, name="pessoa.update"),
    path("pessoa/<int:id>/delete", view_pessoas.destroy, name="pessoa.delete"),
]


