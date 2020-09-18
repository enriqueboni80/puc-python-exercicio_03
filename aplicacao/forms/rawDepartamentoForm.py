from django import forms


class RawDepartamentoForm(forms.Form):
    sigla = forms.CharField()
    descricao = forms.CharField()