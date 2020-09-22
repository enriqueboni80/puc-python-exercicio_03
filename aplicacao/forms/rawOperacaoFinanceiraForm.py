from django import forms
from ..models.classificacaoOperacao import ClassificacaoOperacao
from ..models.tipoOperacao import TipoOperacao


class RawOperacaoFinanceiraEntradaForm(forms.Form):
    valor = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control currency', 'placeholder':'123.56'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    classificao_operacao = forms.ModelChoiceField(queryset=ClassificacaoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    tipo_operacao = forms.ModelChoiceField(queryset=TipoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    data_recebimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder':'dd/mm/aaaa'}), required=False)
    data_previsao = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder':'dd/mm/aaaa'}), required=False)
    situacao = forms.ChoiceField(
        choices=[
            ('1','Recebido'),
            ('2','A Receber'),
        ],
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
    
class RawOperacaoFinanceiraSaidaForm(forms.Form):
    valor = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control currency', 'placeholder':'123.56'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    classificao_operacao = forms.ModelChoiceField(queryset=ClassificacaoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    tipo_operacao = forms.ModelChoiceField(queryset=TipoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    data_vencimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder':'dd/mm/aaaa'}), required=False)
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder':'dd/mm/aaaa'}), required=False)
    situacao = forms.ChoiceField(
        choices=[
            ('1','Pago'),
            ('2','A Pagar'),
        ],
        widget=forms.Select(attrs={'class':'form-control'})
    )