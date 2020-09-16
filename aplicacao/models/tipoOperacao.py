from django.db import models


class TipoOperacao(models.Model):
	nome = models.CharField(max_length=30)
	descricao = models.CharField(max_length=30)
 
	def __str__(self):
		return f"{self.nome}"

	