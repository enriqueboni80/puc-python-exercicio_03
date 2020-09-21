from django.urls import path
from ..views import view_pessoa


urlpatterns = [
    path("", view_pessoa.index, name="pessoa.index"),
    path("create/", view_pessoa.create, name="pessoa.create"),
    path("store/", view_pessoa.store, name="pessoa.store"),
    path("<int:id>/", view_pessoa.show, name="pessoa.show"),
    path("<int:id>/edit", view_pessoa.edit, name="pessoa.edit"),
    path("<int:id>/update", view_pessoa.update, name="pessoa.update"),
    path("<int:id>/delete", view_pessoa.destroy, name="pessoa.delete"),
]


