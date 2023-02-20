from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    logradouro = models.CharField(max_length=200)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome