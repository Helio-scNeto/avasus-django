from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Subforum, Topico
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Topico
class criarTopico(CreateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u'Professores'
    model = Topico
    fields = ['titulo', 'texto']
    template_name = 'pages/cadastro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('topico:listTopico', kwargs={'pk': self.object.subforum.pk})

    def form_valid(self, form):
        subforum = Subforum.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.subforum = subforum
        self.object.user = self.request.user
        self.object.save()
        return super(criarTopico, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subforum'] = Subforum.objects.get(pk=self.kwargs.get('pk'))
        context['titulo'] = "Criar de Tópico"
        context['botao'] = "Criar"

        return context

class listTopico(ListView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u'Professores'
    model = Topico
    template_name = 'lists/topicoList.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subforum'] = Subforum.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        self.topicoList = Topico.objects.filter()
        return self.topicoList






