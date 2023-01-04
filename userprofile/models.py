from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, cpf, password, cidade, estado, aniversario, **extra_fields):
        user = self.model(cpf=cpf,
                          cidade=cidade,
                          estado=estado,
                          aniversario=aniversario,
                          **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, cpf, password, cidade, estado, aniversario,  **extra_fields):
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(cpf, password, cidade, estado, aniversario, **extra_fields)

    def create_superuser(self, cpf, password, cidade, estado, aniversario, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(cpf, password, cidade, estado, aniversario, **extra_fields)


class User(AbstractUser):
    username = None
    cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF')
    nome = models.CharField(max_length=50, verbose_name='Nome completo')
    nomeSocial = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Nome Social')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    password = models.CharField(max_length=11, verbose_name='Senha')
    aniversario = models.DateField(
        max_length=6, verbose_name='Data de Nascimento', null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ['nome', 'nomeSocial',
                       'estado', 'cidade', 'password', 'aniversario']

    objects = UserManager()

    def __str__(self) -> str:
        return self.nome
