# Generated by Django 5.0.1 on 2024-02-15 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='name',
            new_name='vehicle_type',
        ),
    ]
