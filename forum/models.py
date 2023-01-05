from django.db import models
from userprofile.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(unique=True, max_length=30, verbose_name='Nome')

    def __str__(self) -> str:
        return self.nome


class Subforum(models.Model):
    titulo = models.CharField(
        unique=True, max_length=120, blank=False, verbose_name='Título')
    descriçao = models.TextField(
        unique=True, blank=False, verbose_name='Descrição')

    categoria = models.ForeignKey(
        Categoria, blank=False, on_delete=models.PROTECT)

    user = models.ForeignKey(User, blank=False, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo

class Topico(models.Model):
    subforum = models.ForeignKey(Subforum, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Texto', blank=False)

    def __str__(self) -> str:
        return self.texto