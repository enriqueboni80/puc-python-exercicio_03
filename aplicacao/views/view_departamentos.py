from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.departamento import Departamento
from django.template import loader

from ..forms import RawDepartamentoForm


def index(request):
    returnedObjects = Departamento.objects.all()
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "departamento/listar.html", dados)
    
    
def create(request):
    form = RawDepartamentoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "departamento/create.html", dados)


def store(request):
    form = RawDepartamentoForm(request.POST)
    if form.is_valid():
        Departamento.objects.create(**form.cleaned_data)
        return redirect("departamento.index")
    

def show(request, id):
    returnedObject = Departamento.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "departamento/detalhar.html", dados)
    

def edit(request, id):
    returnedObject = Departamento.objects.filter(pk=id).values()[0]
    form = RawDepartamentoForm(returnedObject)
    dados = {"returnedObject": returnedObject, "form": form}
    return render(request, "departamento/edit.html", dados)


def update(request, id):
    returnedObject = Departamento.objects.filter(pk=id)
    form = RawDepartamentoForm(request.POST or None)
    if form.is_valid():
        returnedObject.update(**form.cleaned_data)
        return redirect("departamento.index")
    
    
def destroy(request, idDepartamento):
    Departamento.objects.get(pk=idDepartamento).delete()
    return redirect("departamento.index")
