from django.db import models
from userprofile.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=30, verbose_name='Nome')

    def __str__(self) -> str:
        return self.nome


class Subforum(models.Model):
    titulo = models.CharField(
        unique=True, max_length=120, verbose_name='Título')
    descriçao = models.TextField(
        unique=True, verbose_name='Descrição')

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo
