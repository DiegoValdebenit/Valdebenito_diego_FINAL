# Generated by Django 4.2.4 on 2023-12-22 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminario', '0002_rename_nombre_institucion_nombre_intitucion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institucion',
            old_name='nombre_intitucion',
            new_name='nombre_institucion',
        ),
    ]
