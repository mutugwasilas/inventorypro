# Generated by Django 5.0.1 on 2024-02-26 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_rename_main_inventory_maintenance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='maintenance',
            new_name='main',
        ),
    ]
