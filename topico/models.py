from django.db import models
from forum.models import Subforum
from userprofile.models import User


class Topico(models.Model):
    subforum = models.ForeignKey(
        Subforum, on_delete=models.CASCADE)

    titulo = models.CharField(
        unique=True, max_length=120, blank=False, verbose_name='Título')

    texto = models.TextField(verbose_name='Texto', blank=False)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')

    createdAt = models.DateField(
        auto_now_add=True, verbose_name='Data de criação')

    def __str__(self) -> str:
        return self.titulo

