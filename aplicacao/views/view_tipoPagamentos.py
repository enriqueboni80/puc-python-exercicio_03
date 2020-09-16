from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from ..models.tipoPagamento import TipoPagamento
from django.template import loader

from ..forms import RawTipoPagamentoForm


def index(request):
    returnedObjects = TipoPagamento.objects.all()
    dados = {"returnedObjectsList": returnedObjects}
    return render(request, "tipo-pagamento/listar.html", dados)


def create(request):
    form = RawTipoPagamentoForm(request.POST or None)
    dados = {"form": form}
    return render(request, "tipo-pagamento/create.html", dados)


def store(request):
    if request.method == "POST":
        tipoPagamento = TipoPagamento(
            nome=request.POST["nome"], descricao=request.POST["descricao"],
        )
        tipoPagamento.save()
        return redirect("tipo-pagamento.index")


def show(request, id):
    returnedObject = TipoPagamento.objects.get(pk=id)
    dados = {"returnedObject": returnedObject}
    return render(request, "tipo-pagamento/detalhar.html", dados)


def edit(request, id):
    returnedObject = TipoPagamento.objects.get(pk=id)
    form = RawTipoPagamentoForm({"nome": returnedObject.nome, "descricao": returnedObject.descricao})
    dados = {"returnedObject_id": returnedObject.id, "form": form}
    return render(request, "tipo-pagamento/edit.html", dados)


def update(request, id):
    returnedObject = TipoPagamento.objects.filter(pk=id)
    returnedObject.update(
        nome=request.POST["nome"], descricao=request.POST["descricao"],
    )
    return redirect("tipo-pagamento.index")


def destroy(request, id):
    TipoPagamento.objects.get(pk=id).delete()
    return redirect("tipo-pagamento.index")
