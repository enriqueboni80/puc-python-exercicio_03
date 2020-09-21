from django import forms
from ..models.departamento import Departamento


class RawPessoaForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sobrenome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    idade = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    depto_atual = forms.ModelChoiceField(queryset=Departamento.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    hist_deptos = forms.ModelMultipleChoiceField(queryset=Departamento.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    depto_chefia = forms.ModelChoiceField(queryset=Departamento.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    escolaridade = forms.ChoiceField(
        choices=[
            ("NI", "Não informado"),
            ("EF", "Ensino Fundamental"),
            ("EM", "Ensino Médio"),
            ("ES", "Ensino Superior"),
        ],
        widget=forms.Select(attrs={'class':'form-control'})
    )