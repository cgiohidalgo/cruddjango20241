# Generated by Django 2.2.28 on 2023-03-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20230327_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipoDocumento',
            field=models.CharField(choices=[('PAS', 'Pasaporte'), ('TI', 'Tarjeta de Identidad'), ('CC', 'Cedula de Ciudadania')], max_length=3),
        ),
    ]
