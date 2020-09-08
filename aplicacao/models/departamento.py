from django.db import models


class DepartamentoManager(models.Manager):

	''' Retrieving a single object (departament) '''
	def obter_departamento_por_id(self, idDepartamento):
		result = Departamento.objects.get(pk=idDepartamento)
		return result

	''' Retrieving all departaments '''
	def obter_departamentos(self):
    		result = Departamento.all()
		return results

	''' Retrieving all departaments que contem a sigla '''
	def obter_departamentos_pela_sigla(self, sigla):
    		result = objects.get(headline__contains=sigla)
		return results


class Departamento(models.Model):
	sigla = models.CharField(max_length=6)
	descricao = models.CharField(max_length=30)
 
	def __str__(self):
		return f"{self.descricao}"

	objects = DepartamentoManager()

	