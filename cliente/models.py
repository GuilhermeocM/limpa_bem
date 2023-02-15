from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=200)
    cep = models.CharField(max_length=15)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)