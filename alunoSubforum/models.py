from django.db import models
from forum.models import Subforum
from userprofile.models import User


class AlunoSubforum(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Aluno')
    subforum = models.ForeignKey(
        Subforum, on_delete=models.CASCADE, verbose_name='Subforum')
