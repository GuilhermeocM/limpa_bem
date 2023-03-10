# Generated by Django 4.1.6 on 2023-02-21 07:46

import atendimento.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_alter_funcionario_cargo'),
        ('atendimento', '0008_alter_atendimento_atendente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='atendente',
            field=models.ForeignKey(blank=True, default=atendimento.models.site, on_delete=django.db.models.deletion.DO_NOTHING, related_name='atendimentos', to='funcionario.funcionario'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='helper',
            field=models.ForeignKey(blank=True, default=atendimento.models.guilherme, on_delete=django.db.models.deletion.DO_NOTHING, related_name='atendimentos_helper', to='funcionario.funcionario'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='situacao',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], default='Pendente', max_length=20),
        ),
    ]
