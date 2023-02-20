from django.db import models
from cliente.models import Cliente
from django import forms


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ()
