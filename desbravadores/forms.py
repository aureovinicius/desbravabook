from django import forms
from .models import Desbravador


class DesbravadorForm(forms.ModelForm):
    class Meta:
        model = Desbravador
        fields = ['nome', 'sexo', 'data_nascimento', 'email']