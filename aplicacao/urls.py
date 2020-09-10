from django.urls import path
from . import views

urlpatterns = [
	
	path('',
		views.index, name='index'),
 
 	path('pessoa',
		views.index, name='pessoa.index'),
 
 	path('pessoa/create/',
		views.create, name='pessoa.create'),
  
    path('pessoa/<int:idPessoa>/',
		views.show, name='pessoa.show'),
    
    path('pessoa/<int:idPessoa>/delete',
		views.destroy, name='pessoa.delete'),

]

''' 
|        | GET|HEAD  | categorias                  |                  | App\Http\Controllers\ControladorCategoria@index     | web          | -ok
|        | GET|HEAD  | categorias/novo             |                  | App\Http\Controllers\ControladorCategoria@create    | web          | -ok
|        | POST      | categorias           	   |                  | App\Http\Controllers\ControladorCategoria@store     | web          | -ok
|        | GET|HEAD  | categorias/show/{id}        |                  | App\Http\Controllers\ControladorCategoria@show      | web          | -ok
|        | GET|HEAD  | categorias/apagar/{id}      |                  | App\Http\Controllers\ControladorCategoria@destroy   | web          | -ok
|        | GET|HEAD  | categorias/editar/{id}      |                  | App\Http\Controllers\ControladorCategoria@edit      | web          |
|        | POST      | categorias/{id}             |                  | App\Http\Controllers\ControladorCategoria@update    | web          | 

'''
''' Verb          Path                        Action  Route Name
GET           /users                      index   users.index
GET           /users/create               create  users.create
POST          /users                      store   users.store
GET           /users/{user}               show    users.show
GET           /users/{user}/edit          edit    users.edit
PUT|PATCH     /users/{user}               update  users.update
DELETE        /users/{user}               destroy users.destroy '''