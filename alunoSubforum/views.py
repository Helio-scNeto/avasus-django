from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . models import AlunoSubforum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class alunoSubforum(CreateView, LoginRequiredMixin, GroupRequiredMixin):
    group_required = u'Professores'
    login_url = reverse_lazy('login')
    model = AlunoSubforum
    fields = ['user', 'subforum']
    template_name = 'pages/cadastro.html'
    success_url = reverse_lazy('forumview:listSubforum')

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = super().form_valid(form)
        return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Matricular Aluno"
        context['botao'] = "Matricular"
        return context
