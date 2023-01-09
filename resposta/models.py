from msilib.schema import ListView
from django.db import models
from topico.models import Topico
from userprofile.models import User

# Create your models here.
class Resposta(models.Model):
    topico = models.ForeignKey(
        Topico, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Texto', blank=False)
    createdAt = models.DateField(
        auto_now_add=True, verbose_name='Data de criação')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')
