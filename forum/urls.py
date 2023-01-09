from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import criarSubforum, listSubforum
app_name = 'forumview'

urlpatterns = [
    # SubForum
    path('criarSubforum/', criarSubforum.as_view(), name="criarSubforum"),
    path('listSubforum/', listSubforum.as_view(), name="listSubforum"),
]
