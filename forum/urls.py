from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CadastroSubforum, attSubforum, delSubforum, listSubforum

app_name = 'forumview'

urlpatterns = [
    path('cadastro/', CadastroSubforum.as_view(), name="cadastroSubforum"),
    path('att/<int:pk>/', attSubforum.as_view(), name="attSubforum"),
    path('del/<int:pk>/', delSubforum.as_view(), name="delSubforum"),
    path('list/', listSubforum.as_view(), name="listSubforum"),
]
