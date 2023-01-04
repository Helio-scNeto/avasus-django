from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . models import Subforum
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
class Cadastro(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Subforum
    fields = ['titulo', 'descriçao', 'categoria']
    template_name = 'forumview/cadastro.html'
    success_url = reverse_lazy('forumview:listCadastro')

    def form_valid(self, form):
        form.instance.user = self.request.user

        context = super().form_valid(form)

        context['titulo'] = "Cadastro Subforuns"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context
    


class attCadastro(UpdateView, LoginRequiredMixin):
    model = Subforum
    fields = ['titulo', 'descriçao', 'categoria']
    template_name = 'forumview/cadastro.html'
    success_url = reverse_lazy('forumview:listCadastro')

class delCadastro(DeleteView, LoginRequiredMixin):
    model = Subforum
    template_name = 'forumview/delete.html'
    success_url = reverse_lazy('forumview:listCadastro')


class listCadastro(ListView):
    model = Subforum
    template_name = 'lists/forumList.html'
