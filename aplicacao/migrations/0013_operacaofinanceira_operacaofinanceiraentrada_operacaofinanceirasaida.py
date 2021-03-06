# Generated by Django 3.1 on 2020-09-17 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0012_classificacaooperacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperacaoFinanceira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('descricao', models.CharField(max_length=30)),
                ('classificao_operacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacao.classificacaooperacao')),
                ('tipo_operacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacao.tipooperacao')),
            ],
        ),
        migrations.CreateModel(
            name='OperacaoFinanceiraEntrada',
            fields=[
                ('operacaofinanceira_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacao.operacaofinanceira')),
                ('data_previsao', models.DateField()),
                ('data_recebimento', models.DateField()),
                ('situacao', models.CharField(choices=[('1', 'Recebido'), ('2', 'A Receber')], default='1', max_length=2)),
            ],
            bases=('aplicacao.operacaofinanceira',),
        ),
        migrations.CreateModel(
            name='OperacaoFinanceiraSaida',
            fields=[
                ('operacaofinanceira_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacao.operacaofinanceira')),
                ('data_vencimento', models.DateField()),
                ('data_pagamento', models.DateField()),
                ('situacao', models.CharField(choices=[('1', 'Pago'), ('2', 'A Pagar')], default='1', max_length=2)),
            ],
            bases=('aplicacao.operacaofinanceira',),
        ),
    ]
