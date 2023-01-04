from django import forms
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['cpf','nome', 'nomeSocial', 'estado', 'cidade', 'aniversario']