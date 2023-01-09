from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import Cadastro, listCadastro

app_name = 'userprofile'

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name="cadastro"),
  
    path('cadastro/list/', listCadastro.as_view(), name="listCadastro"),

    path('', auth_views.LoginView.as_view(
        template_name='userprofile/login.html',
    ), name='login'),

    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
