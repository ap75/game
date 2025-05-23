# Generated by Django 5.2 on 2025-05-01 17:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulls_and_cows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='try',
            name='guess',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
