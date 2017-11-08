from django import forms

class VehiculoForm(forms.Form):
    matricula = forms.CharField(unique=True, max_length=40)
    modelo = forms.CharField
    # tipo = forms.ForeignKey(Tipo, on_delete=forms.CASCADE)
    color = forms.CharField
    condicion = forms.CharField
    valor_mercado = forms.IntegerField
from django.forms import ModelForm, TextInput, DateTimeInput
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo', 'direccion', 'fecha_nacimiento']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Nombre'}),
            'apellido': TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'cedula': TextInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Cedula de Identidad'}),
            'correo': TextInput(attrs={'class': 'form-control has-feedback-left', 'placeholder': 'Correo'}),
            'fecha_nacimiento': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'direccion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
        }

        help_texts = {
            'name': ('Escriba el nombre de la persoja e.g Leonardo'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
        }

