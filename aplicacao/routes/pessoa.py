from django.urls import path
from ..views import view_pessoas


urlpatterns = [
    path("", view_pessoas.index, name="pessoa.index"),
    path("create/", view_pessoas.create, name="pessoa.create"),
    path("store/", view_pessoas.store, name="pessoa.store"),
    path("<int:id>/", view_pessoas.show, name="pessoa.show"),
    path("<int:id>/edit", view_pessoas.edit, name="pessoa.edit"),
    path("<int:id>/update", view_pessoas.update, name="pessoa.update"),
    path("<int:id>/delete", view_pessoas.destroy, name="pessoa.delete"),
]


