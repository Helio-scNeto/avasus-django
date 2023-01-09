from django.urls import path
from .views import criarResposta,listResposta

app_name = 'resposta'

urlpatterns = [
    path('criarResposta/<int:pk>/', criarResposta.as_view(), name="criarResposta"),
    path('listResposta/<int:pk>/', listResposta.as_view(), name="listResposta")
]
