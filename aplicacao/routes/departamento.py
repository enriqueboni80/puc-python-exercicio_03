from django.urls import path
from ..views import view_departamento


urlpatterns = [
    path("", view_departamento.index, name="departamento.index"),
    path("create/", view_departamento.create, name="departamento.create"),
    path("store/", view_departamento.store, name="departamento.store"),
    path("<int:id>/", view_departamento.show, name="departamento.show"),
    path("<int:id>/edit", view_departamento.edit, name="departamento.edit"),
    path("<int:id>/update", view_departamento.update, name="departamento.update"),
    path("<int:id>/delete", view_departamento.destroy, name="departamento.delete"),
]

