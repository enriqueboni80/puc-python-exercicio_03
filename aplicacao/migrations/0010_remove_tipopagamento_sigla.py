# Generated by Django 3.1 on 2020-09-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0009_tipopagamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipopagamento',
            name='sigla',
        ),
    ]
