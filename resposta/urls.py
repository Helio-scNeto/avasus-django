from django.urls import path
from .views import criarResposta,feedResposta

app_name = 'resposta'

urlpatterns = [
    path('criarResposta/<int:pk>/', criarResposta.as_view(), name="criarResposta"),

    path('feedResposta/<int:pk>/', feedResposta.as_view(), name="feedResposta")
]
