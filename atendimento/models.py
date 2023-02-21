from django.db import models
from django.utils import timezone
from django import forms
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


    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING, blank=True)
    atendente = models.ForeignKey(Funcionario, blank=True, on_delete=models.DO_NOTHING, related_name="atendimentos")
    helper = models.ForeignKey(Funcionario, blank=True, on_delete=models.DO_NOTHING, related_name="atendimentos_helper")
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    desconto = models.CharField(max_length=20, blank=True)
    valor_pago = models.CharField(max_length=20, blank=True)
    data_hora_cadastro = models.DateTimeField(default=timezone.now)
    data_hora_agendamento = models.DateTimeField()
    forma_pagmento = models.CharField(max_length=20, choices=PAGAMENTO_OPCOES)
    situacao = models.CharField(max_length=20, choices=SITUACAO_OPCOES)


    def __str__(self):
        return self.cliente.nome

    
class FormAtendimento(forms.ModelForm):
    class Meta:
        model = Atendimento
        exclude = ()
