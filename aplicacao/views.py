from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models.pessoa import Pessoa
from django.template import loader


def index(request):
    if request.method == "POST":
        store(request)

    lista_p = Pessoa.objects.all()
    dados = {"listapessoas": lista_p}
    return render(request, "pessoa/listar.html", dados)


def create(request):
    return render(request, "pessoa/create.html")


""" store
show
edit
update
destroy """

def store(request):
    data = Pessoa(
        nome = request.POST['nome'],
        sobrenome = request.POST['sobrenome'],
        idade = request.POST['idade'],
        depto_atual_id = request.POST['depto_atual'],
        depto_chefia_id = None,
        escolaridade = request.POST['escolaridade'],
    )
    data.save()
    return HttpResponse("salvo com sucesso")

def show(request, idPessoa):
    p = Pessoa.objects.get(pk=idPessoa)
    dados = {"pessoa": p}
    return render(request, "pessoa/detalhar.html", dados)

def destroy(request, idPessoa):
    Pessoa.objects.get(pk=idPessoa).delete()
    return redirect('index')
    
def testeJson(request, idPessoa):
    payload = {
        "lista": [
            {"nome": "matheus", "sobrenome": "souza"},
            {"nome": "pedro", "sobrenome": "silva"},
        ]
    }

    return JsonResponse(payload)

