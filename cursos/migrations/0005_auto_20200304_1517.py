# Generated by Django 2.2.10 on 2020-03-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_auto_20200304_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.DecimalField(decimal_places=0, max_digits=11, unique=True),
        ),
    ]