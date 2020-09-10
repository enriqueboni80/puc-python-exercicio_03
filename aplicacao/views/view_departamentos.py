from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.pessoa import Departamento
from django.template import loader


def index(request):
    lista_depto = Departamento.objects.all()
    dados = {"listaDepartamentos": lista_depto}
    return render(request, "departamento/listar.html", dados)


def create(request):
    dados = {"form_action": "departamento.store"}
    return render(request, "departamento/form.html", dados)


def store(request):
    if request.method == "POST":
        departamento = Departamento(
            sigla=request.POST["sigla"],
            descricao=request.POST["descricao"],
        )
        departamento.save()
        return redirect("departamento.index")


def show(request, idDepartamento):
    depto = Departamento.objects.get(pk=idDepartamento)
    dados = {"departamento": depto}
    return render(request, "departamento/detalhar.html", dados)


def edit(request, idDepartamento):
    depto = Departamento.objects.get(pk=idDepartamento)
    dados = {"departamento": depto, "form_action": "departamento.update"}
    return render(request, "departamento/form.html", dados)


def update(request):
    idDepartamento = request.POST["_departamento_id"]
    depto = Departamento.objects.filter(pk=idDepartamento)
    depto.update(
        sigla=request.POST["sigla"],
        descricao=request.POST["descricao"],
    )
    return redirect("departamento.index")


def destroy(request, idDepartamento):
    Departamento.objects.get(pk=idDepartamento).delete()
    return redirect("departamento.index")