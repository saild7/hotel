# Generated by Django 2.1.5 on 2021-02-10 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]