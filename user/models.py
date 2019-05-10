from django.db import models


class User(models.Model):
    nome = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return 'Nome: {}'.format(self.nome)

    class Meta:
        ordering = ['nome']



