# Generated by Django 4.1.6 on 2023-02-19 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('servico', '0001_initial'),
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='atendente',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='funcionario.funcionario'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='desconto',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='helper',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios_helper', to='funcionario.funcionario'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='servico',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='servico.servico'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='valor_pago',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]