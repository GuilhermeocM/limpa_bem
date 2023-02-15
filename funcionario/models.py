from django.db import models

class Funcionario(models.Model):
    CARGO_OPCOES = (
        ("gerente", "Gerente"),
        ("atendente", "Atendente"),
        ("helper", "Helper"),
        )
    cargo = models.CharField(max_length=50, choices=CARGO_OPCOES)
    nome = models.CharField(max_length=200)