# Generated by Django 3.1 on 2020-09-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0015_auto_20200924_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacaofinanceira',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]