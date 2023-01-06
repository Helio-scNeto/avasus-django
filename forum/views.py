from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . models import Subforum, Topico
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# SubForum


class criarSubforum(GroupRequiredMixin, CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Professores"
    model = Subforum
    fields = ['titulo', 'descriçao', 'categoria']
    template_name = 'forumview/cadastro.html'
    success_url = reverse_lazy('forumview:listSubforum')

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = super().form_valid(form)
        # depois do super o bojeto está criado
        return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro Subforuns"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class attSubforum(UpdateView, LoginRequiredMixin):
    model = Subforum
    fields = ['titulo', 'descriçao', 'categoria']
    template_name = 'forumview/cadastro.html'
    success_url = reverse_lazy('forumview:listSubforum')

    def get_object(self):
        self.subforum = Subforum.objects.get(
            pk=self.kwargs['pk'], user=self.request.user)
        return self.subforum

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Atualizar Subforuns"
        context['botao'] = "Salvar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class delSubforum(DeleteView, LoginRequiredMixin):
    model = Subforum
    template_name = 'forumview/delete.html'
    success_url = reverse_lazy('forumview:listSubforum')

    def get_object(self):
        self.subforum = Subforum.objects.get(
            pk=self.kwargs['pk'], user=self.request.user)
        return self.subforum


class listSubforum(ListView, LoginRequiredMixin):
    model = Subforum
    template_name = 'lists/forumList.html'

    def get_queryset(self):
        self.subforumList = Subforum.objects.filter(user=self.request.user)
        return self.subforumList

# Topico

class criarTopico(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Topico
    fields = ['titulo', 'texto']
    template_name = 'forumview/cadastro.html'
    success_url = reverse_lazy('forumview:feedTopico')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        context = super().form_valid(form)
        # depois do super o bojeto está criado
        return context

    def get_object(self):
        self.subforum = Subforum.objects.get(
            pk=self.kwargs['pk'], user=self.request.user)
        return self.subforum

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Criar de Tópico"
        context['botao'] = "Criar"

        return context


class listTopico(ListView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Topico
    template_name = 'lists/topicoList.html'

    def get_queryset(self):
        self.topicoList = Topico.objects.filter()
        return self.topicoList


class feedTopico(ListView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Topico
    template_name = 'forumview/topico.html'

    def get_queryset(self):
        self.feedTopico = Topico.objects.filter(
            pk=self.kwargs['pk'], user=self.request.user)
        return self.feedTopico
