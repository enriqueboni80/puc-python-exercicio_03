from django import forms

    
class RawClassificacaoOperacaoForm(forms.Form):
    nome = forms.CharField()
    descricao = forms.CharField()