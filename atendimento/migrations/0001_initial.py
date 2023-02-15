# Generated by Django 4.1.6 on 2023-02-15 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('servico', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desconto', models.CharField(max_length=20)),
                ('valor_pago', models.CharField(max_length=20)),
                ('data_hora_cadastro', models.CharField(max_length=20)),
                ('data_hora_agendamento', models.CharField(max_length=20)),
                ('forma_pagmento', models.CharField(choices=[('cartao', 'Cartao'), ('especie', 'Especie'), ('boleto', 'Boleto'), ('pix', 'Pix')], max_length=20)),
                ('situacao', models.CharField(choices=[('pendente', 'Pendente'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], max_length=20)),
                ('atendente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='funcionario.funcionario')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('helper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios_helper', to='funcionario.funcionario')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servico.servico')),
            ],
        ),
    ]