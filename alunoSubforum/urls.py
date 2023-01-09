from django.urls import path
from .views import alunoSubforum

app_name = 'alunoSubforum'

urlpatterns = [
    path('alunoSubforum/<int:pk>/', alunoSubforum.as_view(), name="alunoSubforum"),
]
