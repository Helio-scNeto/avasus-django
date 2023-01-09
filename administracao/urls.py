from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CadastraProfessor, listCadastroProfessor, CadastraCategoria, AdminlistSubforum

app_name = 'administracao'

urlpatterns = [
    path('cadastro/', CadastraProfessor.as_view(), name="cadastro"),

    path('cadastro/list/', listCadastroProfessor.as_view(), name="listCadastro"),

    path('listSubforum/list/', AdminlistSubforum.as_view(), name="listCadastro"),

    path('cadastro/categoria/', CadastraCategoria.as_view(),
         name="cadastroCategoria"),
]
