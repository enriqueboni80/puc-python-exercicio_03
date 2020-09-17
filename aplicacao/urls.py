from django.urls import path

from .views import view_home, view_pessoas, view_departamentos, view_tipoOperacoes, view_classificacaoOperacoes, view_operacaoFinanceiraEntradas

urlpatterns = [
    path("", view_home.index, name="index"),
    path("pessoa", view_pessoas.index, name="pessoa.index"),
    path("pessoa/create/", view_pessoas.create, name="pessoa.create"),
    path("pessoa/store/", view_pessoas.store, name="pessoa.store"),
    path("pessoa/<int:id>/", view_pessoas.show, name="pessoa.show"),
    path("pessoa/<int:id>/edit", view_pessoas.edit, name="pessoa.edit"),
    path("pessoa/<int:id>/update", view_pessoas.update, name="pessoa.update"),
    path("pessoa/<int:id>/delete", view_pessoas.destroy, name="pessoa.delete"),
    path("departamento", view_departamentos.index, name="departamento.index"),
    path("departamento/create/", view_departamentos.create, name="departamento.create"),
    path("departamento/store/", view_departamentos.store, name="departamento.store"),
    path("departamento/<int:id>/", view_departamentos.show, name="departamento.show"),
    path("departamento/<int:id>/edit", view_departamentos.edit, name="departamento.edit"),
    path("departamento/<int:id>/update", view_departamentos.update, name="departamento.update"),
    path("departamento/<int:id>/delete", view_departamentos.destroy, name="departamento.delete"),
    path("tipo-operacao", view_tipoOperacoes.index, name="tipo-operacao.index"),
    path("tipo-operacao/create/", view_tipoOperacoes.create, name="tipo-operacao.create"),
    path("tipo-operacao/store/", view_tipoOperacoes.store, name="tipo-operacao.store"),
    path("tipo-operacao/<int:id>/", view_tipoOperacoes.show, name="tipo-operacao.show"),
    path("tipo-operacao/<int:id>/edit", view_tipoOperacoes.edit, name="tipo-operacao.edit"),
    path("tipo-operacao/<int:id>/update", view_tipoOperacoes.update, name="tipo-operacao.update"),
    path("tipo-operacao/<int:id>/delete", view_tipoOperacoes.destroy, name="tipo-operacao.delete"),
    path("classificacao-operacao", view_classificacaoOperacoes.index, name="classificacao-operacao.index"),
    path("classificacao-operacao/create/", view_classificacaoOperacoes.create, name="classificacao-operacao.create"),
    path("classificacao-operacao/store/", view_classificacaoOperacoes.store, name="classificacao-operacao.store"),
    path("classificacao-operacao/<int:id>/", view_classificacaoOperacoes.show, name="classificacao-operacao.show"),
    path("classificacao-operacao/<int:id>/edit", view_classificacaoOperacoes.edit, name="classificacao-operacao.edit"),
    path("classificacao-operacao/<int:id>/update", view_classificacaoOperacoes.update, name="classificacao-operacao.update"),
    path("classificacao-operacao/<int:id>/delete", view_classificacaoOperacoes.destroy, name="classificacao-operacao.delete"),
    
    
    path("operacao-financeira-entrada", view_operacaoFinanceiraEntradas.index, name="operacao-financeira-entrada.index"),
    path("operacao-financeira-entrada/create/", view_operacaoFinanceiraEntradas.create, name="operacao-financeira-entrada.create"),
    path("operacao-financeira-entrada/store/", view_operacaoFinanceiraEntradas.store, name="operacao-financeira-entrada.store"),
    path("operacao-financeira-entrada/<int:id>/", view_operacaoFinanceiraEntradas.show, name="operacao-financeira-entrada.show"),
    path("operacao-financeira-entrada/<int:id>/edit", view_operacaoFinanceiraEntradas.edit, name="operacao-financeira-entrada.edit"),
    path("operacao-financeira-entrada/<int:id>/update", view_operacaoFinanceiraEntradas.update, name="operacao-financeira-entrada.update"),
    path("operacao-financeira-entrada/<int:id>/delete", view_operacaoFinanceiraEntradas.destroy, name="operacao-financeira-entrada.delete"),
    
    
    
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
