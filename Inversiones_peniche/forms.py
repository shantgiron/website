from django import forms

class VehiculoForm(forms.Form):
    matricula = forms.CharField(unique=True, max_length=40)
    modelo = forms.CharField
    # tipo = forms.ForeignKey(Tipo, on_delete=forms.CASCADE)
    color = forms.CharField
    condicion = forms.CharField
    valor_mercado = forms.IntegerField