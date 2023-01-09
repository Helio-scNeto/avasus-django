from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import criarSubforum, attSubforum, delSubforum, listSubforum
app_name = 'forumview'

urlpatterns = [
    # SubForum
    path('criarSubforum/', criarSubforum.as_view(), name="criarSubforum"),

    path('attSubforum/<int:pk>/', attSubforum.as_view(), name="attSubforum"),
    path('delSubforum/<int:pk>/', delSubforum.as_view(), name="delSubforum"),

    path('listSubforum/', listSubforum.as_view(), name="listSubforum"),
]
