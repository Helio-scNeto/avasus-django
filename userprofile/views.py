
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from . models import User 
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import template
from django.urls import reverse_lazy

@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'lists/forumList.html')

class Cadastro(CreateView, SuccessMessageMixin): 
    model = User
    template_name = 'userprofile/cadastro.html'
    form_class = UserForm
    success_url = reverse_lazy('userprofile:login')
    success_message = "Conta foi criada com sucesso!"
    register = template.Library() 

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Alunos')
        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro'
        context ['botao'] = 'Cadastrar'

        return context 

class listCadastro(ListView): 
    model = User
    template_name = 'lists/usersList.html'

