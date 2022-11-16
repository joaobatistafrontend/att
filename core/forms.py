from django import forms

class CurriculoForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    telefone = forms.IntegerField()
    empresa = forms.CharField(max_length=100)
    cargo = forms.CharField(max_length=100)