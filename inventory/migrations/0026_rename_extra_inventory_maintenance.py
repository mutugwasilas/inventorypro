# Generated by Django 5.0.1 on 2024-02-26 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_alter_inventory_extra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='extra',
            new_name='maintenance',
        ),
    ]
