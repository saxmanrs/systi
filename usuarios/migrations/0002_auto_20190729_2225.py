# Generated by Django 2.2.2 on 2019-07-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='inicio',
            field=models.DateField(verbose_name='Data Inicio'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='saida',
            field=models.DateField(null=True, verbose_name='Data de Saida'),
        ),
    ]
