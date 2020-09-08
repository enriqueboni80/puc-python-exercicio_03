from django.urls import path
from . import views

urlpatterns = [
	path('',
		views.indice, name='indice'),

	path('pessoa/<int:idpessoa>/',
		views.pessoa, name='pessoa'),

	path('lista_pessoas/',
		views.lista_pessoas, name='lista_pessoas'),

	path('testeJson/',
		views.testeJson, name='testeJson'),
]