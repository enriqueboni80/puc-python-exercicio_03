# Generated by Django 3.1 on 2020-09-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0013_operacaofinanceira_operacaofinanceiraentrada_operacaofinanceirasaida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacaofinanceiraentrada',
            name='data_previsao',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='operacaofinanceiraentrada',
            name='data_recebimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='operacaofinanceirasaida',
            name='data_pagamento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='operacaofinanceirasaida',
            name='data_vencimento',
            field=models.DateField(null=True),
        ),
    ]
