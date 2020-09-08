from django.shortcuts import render
from rest_framework import viewsets
from .models import Pessoa, Departamento
from .serializers import PessoaSerializer, DepartamentoSerializer

class PessoaViewSet(viewsets.ModelViewSet):
	queryset = Pessoa.objects.all().order_by('nome')[:2]
	serializer_class = PessoaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
	queryset = Departamento.objects.all()
	serializer_class = DepartamentoSerializer