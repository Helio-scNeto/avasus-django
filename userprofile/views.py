from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from . models import User

def home(request):
    return render(request, 'userprofile/base.html')

class Cadastro(CreateView): 
    model = User
    fields = ['nome', 'nomeSocial', 'estado', 'cidade', 'cpf', 'senha1', 'senha2','aniversario']
    template_name = 'userprofile/cadastro.html'
    success_url = reverse_lazy('userprofile:listCadastro')

class attCadastro(UpdateView): 
    model = User
    fields = ['nome', 'nomeSocial', 'estado', 'cidade', 'cpf', 'senha1', 'senha2','aniversario']
    template_name = 'userprofile/cadastro.html'
    success_url = reverse_lazy('userprofile:listCadastro')

class delCadastro(DeleteView): 
    model = User
    template_name = 'userprofile/delete.html'
    success_url = reverse_lazy('home')

class listCadastro(ListView): 
    model = User
    template_name = 'lists/usersList.html'