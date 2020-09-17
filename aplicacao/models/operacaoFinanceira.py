from django.db import models
from .classificacaoOperacao import ClassificacaoOperacao
from .tipoOperacao import TipoOperacao



class OperacaoFinanceira(models.Model):
    
    valor = models.FloatField(null=False)
    descricao = models.CharField(max_length=30)
    
    classificao_operacao = models.ForeignKey(
		ClassificacaoOperacao,
		on_delete=models.RESTRICT,
		null=True)
    
    tipo_operacao = models.ForeignKey(
		TipoOperacao,
		on_delete=models.RESTRICT,
		null=True)
    
    def __str__(self):
        return f"{self.descricao}"

class OperacaoFinanceiraEntrada(OperacaoFinanceira):
    
    data_previsao = models.DateField()
    data_recebimento = models.DateField()
    
    SITUACAO_CHOICES = [
		('1','Recebido'),
		('2','A Receber'),
	]
    
    situacao = models.CharField(
		max_length=2,
		choices=SITUACAO_CHOICES,
		default='1'
	)
    
class OperacaoFinanceiraSaida(OperacaoFinanceira):
    
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    
    SITUACAO_CHOICES = [
		('1','Pago'),
		('2','A Pagar'),
	]
    
    situacao = models.CharField(
		max_length=2,
		choices=SITUACAO_CHOICES,
		default='1'
	)