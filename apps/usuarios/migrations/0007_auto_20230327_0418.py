# Generated by Django 2.2.28 on 2023-03-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20230327_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipoDocumento',
            field=models.CharField(choices=[('TI', 'Tarjeta de Identidad'), ('PAS', 'Pasaporte'), ('CC', 'Cedula de Ciudadania')], max_length=3),
        ),
    ]
