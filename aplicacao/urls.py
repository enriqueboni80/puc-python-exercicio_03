from django.urls import path
from django.urls import include, path


urlpatterns = [
    path('', include('aplicacao.routes.home')),
    path('pessoa', include('aplicacao.routes.pessoa')),
    path('departamento', include('aplicacao.routes.departamento')),
    path('tipo-operacao', include('aplicacao.routes.tipo-operacao')),
    path('classificacao-operacao', include('aplicacao.routes.classificacao-operacao')),
    path('operacao-financeira-entrada', include('aplicacao.routes.operacao-financeira-entrada')),
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
