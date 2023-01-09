from django.urls import path
from .views import alunoSubforum, listSubforum

app_name = 'alunoSubforum'

urlpatterns = [
    path('alunoSubforum/', alunoSubforum.as_view(), name="alunoSubforum"),
    path('alunoSubforum/list', listSubforum.as_view(), name="listSubforum"),
]
