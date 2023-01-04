
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import UserForm
from . models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 


def home(request):
    return render(request, 'userprofile/home.html')

@login_required(login_url='userprofile:login')
def profile(request):
    return render(request, 'userprofile/profile.html')

class Cadastro(CreateView): 
    model = User
    template_name = 'userprofile/cadastro.html'
    form_class = UserForm
    success_url = reverse_lazy('userprofile:login')
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro'
        context ['botao'] = 'Cadastrar'

        return context 
    


class attCadastro(UpdateView): 
    model = User
    fields = ['cpf','nome', 'nomeSocial', 'estado', 'cidade', 'password','aniversario']
    template_name = 'userprofile/cadastro.html'
    success_url = reverse_lazy('userprofile:listCadastro')

class delCadastro(DeleteView): 
    model = User
    template_name = 'userprofile/delete.html'
    success_url = reverse_lazy('userprofile:listCadastro')

class listCadastro(ListView): 
    model = User
    template_name = 'lists/usersList.html'




