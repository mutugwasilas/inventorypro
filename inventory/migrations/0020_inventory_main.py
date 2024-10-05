# Generated by Django 5.0.1 on 2024-02-26 07:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_alter_inventory_cost_per_refuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='main',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
