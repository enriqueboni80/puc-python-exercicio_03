from django.db import models
from django.db.models import Sum, Q
from model_utils.managers import InheritanceManager
from .classificacaoOperacao import ClassificacaoOperacao
from .tipoOperacao import TipoOperacao


class OperacaoFinanceiraManager(InheritanceManager):
    def getElementsOfAllSubClasses(self, dataInicio, dataFim):
        return (
            self.select_subclasses()
            .filter(
                Q(
                    operacaofinanceiraentrada__data_recebimento__gte=dataInicio,
                    operacaofinanceiraentrada__data_recebimento__lte=dataFim,
                )
                | Q(
                    operacaofinanceiraentrada__data_previsao__gte=dataInicio,
                    operacaofinanceiraentrada__data_previsao__lte=dataFim,
                )
                | Q(
                    operacaofinanceirasaida__data_vencimento__gte=dataInicio,
                    operacaofinanceirasaida__data_vencimento__lte=dataFim,
                )
                | Q(
                    operacaofinanceirasaida__data_pagamento__gte=dataInicio,
                    operacaofinanceirasaida__data_pagamento__lte=dataFim,
                )
            )
            .order_by("-id")
        )

    def getSomaRecebidos(self, dataInicio, dataFim):
        soma = (
            self.select_subclasses()
            .filter(
                Q(
                    operacaofinanceiraentrada__data_recebimento__gte=dataInicio,
                    operacaofinanceiraentrada__data_recebimento__lte=dataFim,
                )
            )
            .aggregate(Sum("valor"))["valor__sum"]
        )
        return soma if soma is not None else 00.00
    
    def getSomaAReceber(self, dataInicio, dataFim):
        soma = (
            self.select_subclasses()
            .filter(
                Q(
                    operacaofinanceiraentrada__data_previsao__gte=dataInicio,
                    operacaofinanceiraentrada__data_previsao__lte=dataFim,
                )
            )
            .aggregate(Sum("valor"))["valor__sum"]
        )
        return soma if soma is not None else 00.00
    
    def getSomaPagas(self, dataInicio, dataFim):
        soma = (
            self.select_subclasses()
            .filter(
                Q(
                    operacaofinanceirasaida__data_pagamento__gte=dataInicio,
                    operacaofinanceirasaida__data_pagamento__lte=dataFim,
                )
            )
            .aggregate(Sum("valor"))["valor__sum"]
        )
        return soma if soma is not None else 00.00
    
    def getSomaAPagar(self, dataInicio, dataFim):
        soma = (
            self.select_subclasses()
            .filter(
                Q(
                    operacaofinanceirasaida__data_vencimento__gte=dataInicio,
                    operacaofinanceirasaida__data_vencimento__lte=dataFim,
                )
            )
            .aggregate(Sum("valor"))["valor__sum"]
        )
        return soma if soma is not None else 00.00


class OperacaoFinanceira(models.Model):

    objects = OperacaoFinanceiraManager()

    valor = models.DecimalField(null=False, max_digits=11, decimal_places=2)
    descricao = models.CharField(max_length=30)

    classificao_operacao = models.ForeignKey(
        ClassificacaoOperacao, on_delete=models.RESTRICT, null=True
    )

    tipo_operacao = models.ForeignKey(
        TipoOperacao, on_delete=models.RESTRICT, null=True
    )

    def __str__(self):
        return f"{self.descricao}"


class OperacaoFinanceiraEntrada(OperacaoFinanceira):

    data_previsao = models.DateField(null=True)
    data_recebimento = models.DateField(null=True)

    SITUACAO_CHOICES = [
        ("1", "Recebido"),
        ("2", "A Receber"),
    ]

    situacao = models.CharField(max_length=2, choices=SITUACAO_CHOICES, default="1")


class OperacaoFinanceiraSaida(OperacaoFinanceira):

    data_vencimento = models.DateField(null=True)
    data_pagamento = models.DateField(null=True)

    SITUACAO_CHOICES = [
        ("1", "Pago"),
        ("2", "A Pagar"),
    ]

    situacao = models.CharField(max_length=2, choices=SITUACAO_CHOICES, default="1")

