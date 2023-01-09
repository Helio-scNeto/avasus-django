from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from forum.models import Subforum
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import User
from .forms import UserForm
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django import template
from . models import Categoria
from django.contrib import messages

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class CadastraCategoria(CreateView, LoginRequiredMixin, SuccessMessageMixin,SuperuserRequiredMixin): 
    model = Categoria
    template_name = 'pages/cadastro.html'
    fields = ['nome']
    success_message = "Categoria foi criada com sucesso!"
    success_url = reverse_lazy('administracao:cadastroCategoria')

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro Categoria'
        context ['botao'] = 'Cadastrar'
        return context 

class CadastraProfessor(CreateView, LoginRequiredMixin, SuccessMessageMixin,SuperuserRequiredMixin): 
    model = User
    template_name = 'pages/cadastro.html'
    form_class = UserForm
    success_url = reverse_lazy('administracao:cadastro')
    success_message = "Professor cadastrado com sucesso!"
    register = template.Library()

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data 

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Professores')
        answer = super().form_valid(form)

        success_message = self.get_success_message(form.cleaned_data)

        self.object.groups.add(grupo)
        self.object.save()

        if success_message:
            messages.success(self.request, success_message)

        return answer
        

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Professor'
        context ['botao'] = 'Cadastrar'

        return context 

class listCadastroProfessor(ListView, LoginRequiredMixin, SuperuserRequiredMixin): 
    model = User
    template_name = 'lists/usersList.html'

    def get_queryset(self):
        self.UserList = User.objects.all()
        return self.UserList

class AdminlistSubforum(ListView, LoginRequiredMixin, SuperuserRequiredMixin):
    model = Subforum
    template_name = 'lists/adminforumList.html'
    register = template.Library() 

    def get_queryset(self):
        self.subforumList = Subforum.objects.all()
        return self.subforumList