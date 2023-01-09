
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Resposta, Topico
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class criarResposta(CreateView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u'Professores'
    model = Resposta
    fields = ['texto']
    template_name = 'pages/cadastro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('resposta:listResposta', kwargs={'pk': self.object.topico.pk})

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
        context['titulo'] = "Criar de Resposta"
        context['botao'] = "Responder"

        return context

class listResposta(ListView, LoginRequiredMixin, GroupRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = [u'Professores', u'Alunos']
    model = Resposta
    template_name = 'resposta/resposta.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['topico'] = Topico.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        self.respostaList = Resposta.objects.filter()
        return self.respostaList