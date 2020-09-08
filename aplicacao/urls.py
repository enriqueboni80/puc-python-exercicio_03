from django.urls import path
from . import views

urlpatterns = [
	path('pessoa',
		views.index, name='index'),
 
 	path('pessoa/novo/',
		views.create, name='novo'),

	path('pessoa/editar/<int:idpessoa>/',
		views.pessoa, name='editar'),

	path('testeJson/',
		views.testeJson, name='testeJson'),
]

''' 
|        | GET|HEAD  | categorias                  |                  | App\Http\Controllers\ControladorCategoria@index     | web          | -ok
|        | GET|HEAD  | categorias/novo             |                  | App\Http\Controllers\ControladorCategoria@create    | web          | -ok
|        | POST      | categorias                  |                  | App\Http\Controllers\ControladorCategoria@store     | web          |
|        | GET|HEAD  | categorias/apagar/{id}      |                  | App\Http\Controllers\ControladorCategoria@destroy   | web          |
|        | GET|HEAD  | categorias/editar/{id}      |                  | App\Http\Controllers\ControladorCategoria@edit      | web          |
|        | POST      | categorias/{id}             |                  | App\Http\Controllers\ControladorCategoria@update    | web          | 
'''