from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.pessoa import Pessoa
from ..models.departamento import Departamento
from django.template import loader

from ..forms import RawPessoaForm


""" return HttpResponse("Chegou aqui") """


def index(request):
    returnedObjects = Pessoa.objects.all().order_by('-id')
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "pessoa/listar.html", dados)


def create(request):
    form = RawPessoaForm(request.POST or None)
    dados = {"form": form, "qtdDepartamentos": Departamento.objects.count()}
    return render(request, "pessoa/create.html", dados)


def store(request):
    form = RawPessoaForm(request.POST)
    if form.is_valid():       
        instance = Pessoa.objects.create(
            nome=form.cleaned_data.get("nome"),
            sobrenome=form.cleaned_data.get("sobrenome"),
            idade=form.cleaned_data.get("idade"),
            depto_atual=form.cleaned_data.get("depto_atual"),
            depto_chefia=form.cleaned_data.get("depto_chefia"),
            escolaridade=form.cleaned_data.get("escolaridade"),
        )
        instance.hist_deptos.set(form.cleaned_data.get("hist_deptos"))
        return redirect("pessoa.index")

def show(request, id):
    returnedObject = Pessoa.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "pessoa/detalhar.html", dados)

def edit(request, id):
    returnedObject = Pessoa.objects.filter(pk=id).values()[0]
    form = RawPessoaForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "pessoa/edit.html", dados)


def update(request, id):
    returnedObject = Pessoa.objects.filter(pk=id)
    form = RawPessoaForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(
            nome=form.cleaned_data.get("nome"),
            sobrenome=form.cleaned_data.get("sobrenome"),
            idade=form.cleaned_data.get("idade"),
            depto_atual=form.cleaned_data.get("depto_atual"),
            depto_chefia=form.cleaned_data.get("depto_chefia"),
            escolaridade=form.cleaned_data.get("escolaridade"),
        )
        ''' returnedObject.hist_deptos.set(form.cleaned_data.get("hist_deptos")) '''
        return redirect("pessoa.index")
    
def destroy(request, id):
    Pessoa.objects.get(pk=id).delete()
    return redirect("pessoa.index")
