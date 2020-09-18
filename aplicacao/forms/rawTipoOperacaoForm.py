from django import forms


class RawTipoOperacaoForm(forms.Form):
    nome = forms.CharField()
    descricao = forms.CharField()
