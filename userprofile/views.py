
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from . models import User
from django.contrib.auth import authenticate, login 
from django.shortcuts import render

def home(request):
    return render(request, 'userprofile/base.html')

class Cadastro(CreateView): 
    model = User
    fields = ['cpf','nome', 'nomeSocial', 'estado', 'cidade', 'password','aniversario']
    template_name = 'userprofile/cadastro.html'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['título'] = 'Registor de novo usuário'
        context ['botão'] = 'Cadastrar'

        return context 
    # success_url = reverse_lazy('userprofile:login')


class attCadastro(UpdateView): 
    model = User
    fields = ['cpf','nome', 'nomeSocial', 'estado', 'cidade', 'password','aniversario']
    template_name = 'userprofile/cadastro.html'
    success_url = reverse_lazy('userprofile:listCadastro')

class delCadastro(DeleteView): 
    model = User
    template_name = 'userprofile/delete.html'
    success_url = reverse_lazy('home')

class listCadastro(ListView): 
    model = User
    template_name = 'lists/usersList.html'




