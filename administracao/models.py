from django.db import models
from userprofile.models import User

class Categoria(models.Model):
    nome = models.CharField(unique=False, max_length=30, verbose_name='Nome')
    
    def __str__(self) -> str:
        return self.nome