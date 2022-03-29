from django import forms
from django.forms import fields, widgets
from .models import Usuario
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('cpf',)
        labels = {
            'cpf': 'Digite seu CPF',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
