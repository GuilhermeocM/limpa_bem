from django.db import models

class Servico(models.Model):
    CATEGORIA_OPCOES = (
        ("profundo", "Profundo"),
        ("simples", "Simples")
        )
    categoria = models.CharField(max_length=30, choices=CATEGORIA_OPCOES)
    valor = models.FloatField()