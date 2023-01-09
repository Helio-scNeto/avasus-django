from django import forms
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import User
from .models import Categoria

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['cpf','nome', 'nomeSocial', 'estado', 'cidade', 'aniversario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class':'mask-cpf'})
        self.fields['aniversario'].widget.attrs.update({'class':'mask-aniversario'})


