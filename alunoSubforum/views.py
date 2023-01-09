from django.views.generic.list import ListView
from . models import AlunoSubforum, Subforum
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class alunoSubforum(ListView, LoginRequiredMixin, GroupRequiredMixin):
    group_required = u'Professores'
    login_url = reverse_lazy('login')
    model = AlunoSubforum
    template_name = 'lists/forumList.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['subforum'] = Subforum.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        self.topicoList = Subforum.objects.filter(user=self.request.user)
        return self.topicoList


   