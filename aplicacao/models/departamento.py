from django.db import models


class DepartamentoManager(models.Manager):

	''' Retrieving a single object (departament) '''
	def obter_departamento_por_id(self, idDepartamento):
		result = Departamento.objects.get(pk=idDepartamento)
		return result

	''' Retrieving all departaments (departament) '''
	def obter_todos_departamentos(self):
		results = Departamento.objects.all()
		return results

	''' Retrieving all departaments que contem a sigla  '''
	def obter_departamentos_pela_sigla(self, sigla):
		results = Departamento.objects.get(sigla__contains='FIN')
		return results


class Departamento(models.Model):
	sigla = models.CharField(max_length=6)
	descricao = models.CharField(max_length=30)
 
	def __str__(self):
		return f"{self.descricao}"

	objects = DepartamentoManager()

	