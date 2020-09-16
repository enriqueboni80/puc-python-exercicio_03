from django.urls import path
from .views import view_home, view_pessoas, view_departamentos, view_tipoOperacoes

urlpatterns = [
    path("", view_home.index, name="index"),
    path("pessoa", view_pessoas.index, name="pessoa.index"),
    path("pessoa/create/", view_pessoas.create, name="pessoa.create"),
    path("pessoa/store/", view_pessoas.store, name="pessoa.store"),
    path("pessoa/<int:idPessoa>/", view_pessoas.show, name="pessoa.show"),
    path("pessoa/<int:idPessoa>/edit", view_pessoas.edit, name="pessoa.edit"),
    path("pessoa/<int:idPessoa>/update", view_pessoas.update, name="pessoa.update"),
    path("pessoa/<int:idPessoa>/delete", view_pessoas.destroy, name="pessoa.delete"),
    path("departamento", view_departamentos.index, name="departamento.index"),
    path("departamento/create/", view_departamentos.create, name="departamento.create"),
    path("departamento/store/", view_departamentos.store, name="departamento.store"),
    path("departamento/<int:idDepartamento>/", view_departamentos.show, name="departamento.show"),
    path("departamento/<int:idDepartamento>/edit", view_departamentos.edit, name="departamento.edit"),
    path("departamento/<int:idDepartamento>/update", view_departamentos.update, name="departamento.update"),
    path("departamento/<int:idDepartamento>/delete", view_departamentos.destroy, name="departamento.delete"),
    path("tipo-operacao", view_tipoOperacoes.index, name="tipo-operacao.index"),
    path("tipo-operacao/create/", view_tipoOperacoes.create, name="tipo-operacao.create"),
    path("tipo-operacao/store/", view_tipoOperacoes.store, name="tipo-operacao.store"),
    path("tipo-operacao/<int:id>/", view_tipoOperacoes.show, name="tipo-operacao.show"),
    path("tipo-operacao/<int:id>/edit", view_tipoOperacoes.edit, name="tipo-operacao.edit"),
    path("tipo-operacao/<int:id>/update", view_tipoOperacoes.update, name="tipo-operacao.update"),
    path("tipo-operacao/<int:id>/delete", view_tipoOperacoes.destroy, name="tipo-operacao.delete"),
    

]

""" MODELOS DOS VERBOS
Verb          Path                          Action  Route Name
GET           /pessoa                       index   users.index
GET           /pessoa/create                create  users.create
POST          /pessoa/store                 store   users.store
GET           /pessoa/{idPessoa}            show    users.show
GET           /pessoa/{idPessoa}/edit       edit    users.edit
PUT|PATCH     /pessoa/{idPessoa}/update     update  users.update
DELETE        /pessoa/{idPessoa}            destroy users.destroy 
"""
