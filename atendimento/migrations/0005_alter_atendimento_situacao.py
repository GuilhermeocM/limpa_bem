# Generated by Django 4.1.6 on 2023-02-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0004_alter_atendimento_atendente_alter_atendimento_helper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='situacao',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], default='', max_length=20),
        ),
    ]
