from django.db import models


class DepartamentoManager(models.Manager):


	def obter_departamento_por_id(self, idDepartamento):
		result = Departamento.objects.get(pk=idDepartamento)
		return result


class Departamento(models.Model):
	sigla = models.CharField(max_length=6)
	descricao = models.CharField(max_length=30)
 
	def __str__(self):
		return f"{self.descricao}"

	objects = DepartamentoManager()

	