from django import forms
from ..models.classificacaoOperacao import ClassificacaoOperacao
from ..models.tipoOperacao import TipoOperacao
from ..helpers.constantes import Constantes



class RawOperacaoFinanceiraEntradaForm(forms.Form):    
    valor = forms.CharField(localize=True, widget=forms.TextInput(attrs={'class':'form-control currency', 'placeholder':'123,56'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    classificao_operacao = forms.ModelChoiceField(queryset=ClassificacaoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    tipo_operacao = forms.ModelChoiceField(queryset=TipoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    data_recebimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)
    data_previsao = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)
    situacao = forms.ChoiceField(
        choices=[
            (Constantes.RECEBIDO,'Recebido'),
            (Constantes.ARECEBER,'A Receber'),
        ],
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
    
class RawOperacaoFinanceiraSaidaForm(forms.Form):
    valor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control currency', 'placeholder':'123,56'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    classificao_operacao = forms.ModelChoiceField(queryset=ClassificacaoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    tipo_operacao = forms.ModelChoiceField(queryset=TipoOperacao.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    data_pagamento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)
    data_vencimento = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)
    situacao = forms.ChoiceField(
        choices=[
            (Constantes.PAGO,'Pago'),
            (Constantes.APAGAR,'A Pagar'),
        ],
        widget=forms.Select(attrs={'class':'form-control'})
    )
    
class RawPesquisarPorDataForm(forms.Form):
    data_inicio = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)
    data_fim = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa', 'data-mask':"00/00/0000"}), required=False)