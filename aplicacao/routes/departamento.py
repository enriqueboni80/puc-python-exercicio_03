from django.urls import path
from ..views import view_departamentos


urlpatterns = [
    path("departamento", view_departamentos.index, name="departamento.index"),
    path("departamento/create/", view_departamentos.create, name="departamento.create"),
    path("departamento/store/", view_departamentos.store, name="departamento.store"),
    path("departamento/<int:id>/", view_departamentos.show, name="departamento.show"),
    path("departamento/<int:id>/edit", view_departamentos.edit, name="departamento.edit"),
    path("departamento/<int:id>/update", view_departamentos.update, name="departamento.update"),
    path("departamento/<int:id>/delete", view_departamentos.destroy, name="departamento.delete"),
]

