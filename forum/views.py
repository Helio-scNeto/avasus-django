from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from . models import Subforum
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
# Create your views here.


class CadastroSubforum(GroupRequiredMixin,CreateView, LoginRequiredMixin):
    group_required = u"Professores"
    login_url = reverse_lazy('login')
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
