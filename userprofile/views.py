from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from . models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django import template
from django.urls import reverse_lazy
from django.contrib import messages


@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'userprofile/profile.html')


class Cadastro(CreateView, SuccessMessageMixin):
    model = User
    template_name = 'pages/cadastro.html'
    form_class = UserForm
    success_url = reverse_lazy('userprofile:login')
    success_message = "Conta foi criada com sucesso!"
    register = template.Library()

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Alunos')
        answer = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return answer

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro'
        context['botao'] = 'Cadastrar'

        return context
