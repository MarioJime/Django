# Generated by Django 4.1.7 on 2023-03-05 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='descripcion1',
            new_name='descripcion',
        ),
    ]