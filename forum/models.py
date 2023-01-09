from django.db import models
from userprofile.models import User
from administracao.models import Categoria

class Subforum(models.Model):
    titulo = models.CharField(
        unique=True, max_length=120, blank=False, verbose_name='Título')
    descriçao = models.TextField(
        unique=True, blank=False, verbose_name='Descrição')

    categoria = models.ForeignKey(
        Categoria, blank=False, on_delete=models.PROTECT)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

class AlunoSubforum(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    subforum = models.ForeignKey(
        Subforum, on_delete=models.CASCADE)
