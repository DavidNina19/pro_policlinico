# Generated by Django 5.2.1 on 2025-07-05 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hora',
            old_name='codHora',
            new_name='codHor',
        ),
    ]
