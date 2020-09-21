from django import forms

    
class RawClassificacaoOperacaoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))