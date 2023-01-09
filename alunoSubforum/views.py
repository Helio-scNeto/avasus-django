from django.views.generic.edit import CreateView
from userprofile.models import User
from forum.models import Subforum
from . models import AlunoPermitido
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin

class alunoSubforum(CreateView, LoginRequiredMixin, GroupRequiredMixin):
    group_required = u'Professores'
    login_url = reverse_lazy('login')
    model = AlunoPermitido
    fields = ['user', 'subforum']
    template_name = 'pages/cadastro.html'
    success_url = reverse_lazy('forumview:listSubforum')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = User.objects.filter(groups=1)
        context['titulo'] = "Adicionar Aluno"
        context['botao'] = "Adicionar"
        self.object.user = self.request.user
        return context


class listSubforum(ListView, LoginRequiredMixin, GroupRequiredMixin):
    group_required = u'Alunos'
    model = AlunoPermitido
    template_name = 'lists/matriculaList.html'

    def get_queryset(self):
        permitido = AlunoPermitido.objects.get(user=self.request.user)
        subforum = Subforum.objects.filter(pk=permitido.subforum.pk)
        return subforum



    
