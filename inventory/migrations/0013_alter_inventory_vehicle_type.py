# Generated by Django 5.0.1 on 2024-02-18 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_inventory_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='vehicle_type',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(regex='^[a-zA-Z0-9]*$')]),
        ),
    ]
