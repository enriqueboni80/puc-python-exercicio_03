from django import forms


class RawDepartamentoForm(forms.Form):
    sigla = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))