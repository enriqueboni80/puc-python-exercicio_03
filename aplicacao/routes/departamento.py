from django.urls import path
from ..views import view_departamentos


urlpatterns = [
    path("", view_departamentos.index, name="departamento.index"),
    path("create/", view_departamentos.create, name="departamento.create"),
    path("store/", view_departamentos.store, name="departamento.store"),
    path("<int:id>/", view_departamentos.show, name="departamento.show"),
    path("<int:id>/edit", view_departamentos.edit, name="departamento.edit"),
    path("<int:id>/update", view_departamentos.update, name="departamento.update"),
    path("<int:id>/delete", view_departamentos.destroy, name="departamento.delete"),
]

