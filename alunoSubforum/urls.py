from django.urls import path
from .views import alunoSubforum

app_name = 'alunoSubforum'

urlpatterns = [
    path('alunoSubforum/', alunoSubforum.as_view(), name="alunoSubforum"),
]
