from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome
