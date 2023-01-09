from django import forms
from django.contrib.auth.forms import UserCreationForm
from topico.models import Topico


class UserForm(UserCreationForm):
    class Meta:
        model = Topico
        fields = []