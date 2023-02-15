from django.db import models
from servico.models import Servico
from funcionario.models import Funcionario
from cliente.models import Cliente

class Atendimento(models.Model):
    PAGAMENTO_OPCOES = (
        ("cartao", "Cartao"),
        ("especie", "Especie"),
        ("boleto", "Boleto"),
        ("pix", "Pix"),
        )
    SITUACAO_OPCOES = (
        ("pendente", "Pendente"),
        ("realizado", "Realizado"),
        ("cancelado", "Cancelado"),
        )


    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    atendente = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="funcionarios")
    helper = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="funcionarios_helper")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    desconto = models.CharField(max_length=20)
    valor_pago = models.CharField(max_length=20)
    data_hora_cadastro = models.CharField(max_length=20)
    data_hora_agendamento = models.CharField(max_length=20)
    forma_pagmento = models.CharField(max_length=20, choices=PAGAMENTO_OPCOES)
    situacao = models.CharField(max_length=20, choices=SITUACAO_OPCOES)
