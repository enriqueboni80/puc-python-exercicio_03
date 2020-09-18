from django import forms
from ..models.classificacaoOperacao import ClassificacaoOperacao
from ..models.tipoOperacao import TipoOperacao


class RawOperacaoFinanceiraEntradaForm(forms.Form):
    valor = forms.FloatField()
    descricao = forms.CharField()
    classificao_operacao = forms.ModelChoiceField(queryset=ClassificacaoOperacao.objects.all())
    tipo_operacao = forms.ModelChoiceField(queryset=TipoOperacao.objects.all())
    data_previsao = forms.DateField()
    data_recebimento = forms.DateField()
    situacao = forms.ChoiceField(
        choices=[
            ('1','Recebido'),
            ('2','A Receber'),
        ]
    )