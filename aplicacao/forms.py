from django import forms
from .models.departamento import Departamento
from .models.pessoa import Pessoa


class RawDepartamentoForm(forms.Form):
    sigla = forms.CharField()
    descricao = forms.CharField()
    
    
class RawTipoPagamentoForm(forms.Form):
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

