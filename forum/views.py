from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from . models import Subforum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django import template

# SubForum
class criarSubforum(GroupRequiredMixin, CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    group_required = u"Professores"
    model = Subforum
    fields = ['titulo', 'descriçao', 'categoria']
    template_name = 'pages/cadastro.html'
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
        return context


# class attSubforum(UpdateView, LoginRequiredMixin):
#     model = Subforum
#     fields = ['titulo', 'descriçao', 'categoria']
#     template_name = 'forumview/cadastro.html'
#     success_url = reverse_lazy('forumview:listSubforum')

#     def get_object(self):
#         self.subforum = Subforum.objects.get(
#             pk=self.kwargs['pk'], user=self.request.user)
#         return self.subforum

#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['titulo'] = "Atualizar Subforuns"
#         context['botao'] = "Salvar"

#         return context

# class delSubforum(DeleteView, LoginRequiredMixin):
#     model = Subforum
#     template_name = 'forumview/delete.html'
#     success_url = reverse_lazy('forumview:listSubforum')

#     def get_object(self):
#         self.subforum = Subforum.objects.get(
#             pk=self.kwargs['pk'],
#             user=self.request.user)
#         return self.subforum

class listSubforum(ListView, LoginRequiredMixin):
    group_required = u"Professores"
    model = Subforum
    template_name = 'lists/forumList.html'

    register = template.Library() 

    def get_queryset(self):
        self.subforumList = Subforum.objects.filter(user=self.request.user)
        return self.subforumList





