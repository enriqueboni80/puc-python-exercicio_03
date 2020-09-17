from django import forms
from .models.departamento import Departamento
from .models.pessoa import Pessoa
from .models.classificacaoOperacao import ClassificacaoOperacao
from .models.tipoOperacao import TipoOperacao
from .models.operacaoFinanceira import OperacaoFinanceiraEntrada


class RawDepartamentoForm(forms.Form):
    sigla = forms.CharField()
    descricao = forms.CharField()
    
    
class RawTipoOperacaoForm(forms.Form):
    nome = forms.CharField()
    descricao = forms.CharField()
    
class RawClassificacaoOperacaoForm(forms.Form):
    nome = forms.CharField()
    descricao = forms.CharField()


class RawPessoaForm(forms.Form):
    nome = forms.CharField()
    sobrenome = forms.CharField()
    idade = forms.IntegerField()
    depto_atual = forms.ModelChoiceField(queryset=Departamento.objects.all())
    hist_deptos = forms.ModelMultipleChoiceField(queryset=Departamento.objects.all(), required=False)
    depto_chefia = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False)
    escolaridade = forms.ChoiceField(
        choices=[
            ("NI", "Não informado"),
            ("EF", "Ensino Fundamental"),
            ("EM", "Ensino Médio"),
            ("ES", "Ensino Superior"),
        ]
    )
    
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
    

