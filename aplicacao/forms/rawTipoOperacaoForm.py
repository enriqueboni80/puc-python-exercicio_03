from django import forms


class RawTipoOperacaoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
