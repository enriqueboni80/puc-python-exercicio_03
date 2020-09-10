from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pessoa", views.index, name="pessoa.index"),
    path("pessoa/create/", views.create, name="pessoa.create"),
    path("pessoa/store/", views.store, name="pessoa.store"),
    path("pessoa/<int:idPessoa>/", views.show, name="pessoa.show"),
    path("pessoa/<int:idPessoa>/edit", views.edit, name="pessoa.edit"),
    path("pessoa/update", views.update, name="pessoa.update"),
    path("pessoa/<int:idPessoa>/delete", views.destroy, name="pessoa.delete"),
]

""" VERBS
Verb          Path                        Action  Route Name
GET           /pessoa                     index   users.index
GET           /pessoa/create              create  users.create
POST          /pessoa/store               store   users.store
GET           /pessoa/{idPessoa}          show    users.show
GET           /pessoa/{idPessoa}/edit     edit    users.edit
PUT|PATCH     /pessoa/update              update  users.update
DELETE        /pessoa/{idPessoa}          destroy users.destroy 
"""
