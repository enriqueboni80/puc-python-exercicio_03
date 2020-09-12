from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.departamento import Departamento
from django.template import loader

from ..forms import RawDepartamentoForm


def index(request):
    lista_depto = Departamento.objects.all()
    dados = {"listaDepartamentos": lista_depto}
    return render(request, "departamento/listar.html", dados)


def create(request):
    form = RawDepartamentoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "departamento/create.html", dados)


def store(request):
    if request.method == "POST":
        departamento = Departamento(
            sigla=request.POST["sigla"], descricao=request.POST["descricao"],
        )
        departamento.save()
        return redirect("departamento.index")


def show(request, idDepartamento):
    depto = Departamento.objects.get(pk=idDepartamento)
    dados = {"departamento": depto}
    return render(request, "departamento/detalhar.html", dados)


def edit(request, idDepartamento):
    depto = Departamento.objects.get(pk=idDepartamento)
    form = RawDepartamentoForm({"sigla": depto.sigla, "descricao": depto.descricao})
    dados = {"depto_id": depto.id, "form": form}
    return render(request, "departamento/edit.html", dados)


def update(request, idDepartamento):
    depto = Departamento.objects.filter(pk=idDepartamento)
    depto.update(
        sigla=request.POST["sigla"], descricao=request.POST["descricao"],
    )
    return redirect("departamento.index")


def destroy(request, idDepartamento):
    Departamento.objects.get(pk=idDepartamento).delete()
    return redirect("departamento.index")
