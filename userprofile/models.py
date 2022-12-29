from django.db import models


class User(models.Model):
    nome = models.CharField(max_length=50)
    nomeSocial = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    senha1 = models.CharField(max_length=11)
    senha2 = models.CharField(max_length=11)
    aniversario = models.DateField(max_length=6)

    def __str__(self):
        return "{} ({})".format(self.nome, self.cpf)
