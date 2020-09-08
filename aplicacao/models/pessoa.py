from django.db import models
from .departamento import Departamento

class PessoaManager(models.Manager):
	'''
		Retorna maiores de 18
	'''
	def obter_pessoas_adultas(self):
		result = Pessoa.objects.filter(
			idade__gte=18)
		return result

class Pessoa(models.Model):
	nome = models.CharField(max_length=30)
	sobrenome = models.CharField(max_length=30)
	idade = models.IntegerField(null=True)

	depto_atual = models.ForeignKey(
		Departamento,
		on_delete=models.RESTRICT,
		null=True)

	hist_deptos = models.ManyToManyField(
		Departamento,
		related_name='hist_pessoa_depto')

	depto_chefia = models.OneToOneField(
		Departamento,
		on_delete=models.RESTRICT,
		null=True,
		related_name='chefia_depto')

	ESCOLARIDADE_CHOICES = [
		('NI','Não informado'),
		('EF','Ensino Fundamental'),
		('EM','Ensino Médio'),
		('ES','Ensino Superior'),
	]

	escolaridade = models.CharField(
		max_length=2,
		choices=ESCOLARIDADE_CHOICES,
		default='NI'
	)

	def __str__(self):
		return f"{self.nome} ({self.id})"

	objects = PessoaManager()