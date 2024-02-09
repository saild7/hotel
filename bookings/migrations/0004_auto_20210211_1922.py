# Generated by Django 2.1.5 on 2021-02-11 13:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20210210_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(10)]),
        ),
    ]
