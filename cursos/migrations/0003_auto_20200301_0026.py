# Generated by Django 2.2.10 on 2020-03-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.DecimalField(decimal_places=0, max_digits=11, unique=True),
        ),
    ]
