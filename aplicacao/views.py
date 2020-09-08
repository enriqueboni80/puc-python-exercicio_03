from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.pessoa import Pessoa
from django.template import loader


def index(request):
    	# Aqui é o modelo
	lista_p = Pessoa.objects.obter_pessoas_adultas()
	dados = { 'listapessoas' : lista_p }

	# Aqui é o template
	template = loader.get_template('pessoa/listar.html')
	return HttpResponse(
		template.render(dados, request)
	)

def create(request):
     return render(request, 'pessoa/create.html')
 
''' store
show
edit
update
destroy '''

def pessoa(request, idpessoa):
	p = Pessoa.objects.get(pk=idpessoa)
	dados = {'pessoa':p}
	return render(request, 'pessoa/detalhar.html', dados)












def testeJson(request):
	payload = {'lista':[
		{
			'nome':'matheus',
			'sobrenome':'souza'
		},
		{
			'nome':'pedro',
			'sobrenome':'silva'
		}
	]}
	
	return JsonResponse(payload)