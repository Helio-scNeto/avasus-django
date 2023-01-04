from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import Cadastro, attCadastro, delCadastro, listCadastro

app_name = 'forumview'

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name="cadastro"),
    path('cadastro/att/<int:pk>/', attCadastro.as_view(), name="attCadastro"),
    path('cadastro/del/<int:pk>/', delCadastro.as_view(), name="delCadastro"),
    path('cadastro/list/', listCadastro.as_view(), name="listCadastro"),
]
