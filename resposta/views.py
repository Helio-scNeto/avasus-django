
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Resposta, Topico
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404


class criarResposta(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Resposta
    fields = ['texto']
    template_name = 'resposta/cadastro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('resposta:feedResposta', kwargs={'pk': self.object.topico.pk})

    def form_valid(self, form):
        topico = Topico.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.topico = topico
        self.object.user = self.request.user
        self.object.save()
        return super(criarResposta, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['topico'] = Topico.objects.get(pk=self.kwargs.get('pk'))
        context['titulo'] = "Responder tópico"
        context['botao'] = "Responder"

        return context

class feedResposta(ListView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Topico
    template_name = 'topico/topico.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['topico'] = Topico.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        self.feedResposta = Topico.objects.filter()
        return self.feedResposta