from django.urls import path
from .views import criarTopico, listTopico

app_name = 'topico'

urlpatterns = [
    path('criarTopico/<int:pk>/', criarTopico.as_view(), name="criarTopico"),
    path('listTopico/<int:pk>/', listTopico.as_view(), name="listTopico"),
]
