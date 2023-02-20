from django.db import models

class Servico(models.Model):
    CATEGORIA_OPCOES = (
        ("Profundo", "Profundo"),
        ("Simples", "Simples")
        )
    categoria = models.CharField(max_length=30, choices=CATEGORIA_OPCOES)
    valor = models.FloatField()

    def __str__(self):
        return self.categoria