# Generated by Django 2.2.28 on 2023-03-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20230327_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ciudad',
            field=models.CharField(choices=[('B/Q', 'Barranquilla'), ('CALI', 'Cali'), ('CUC', 'Cucuta'), ('MED', 'Medellín'), ('BOG', 'Bogotá'), ('BCM', 'Bucaramanga'), ('SOL', 'Soledad'), ('SOAC', 'Soacha'), ('CART', 'Cartagena'), ('IBG', 'Ibague')], default='CALI', max_length=4),
        ),
        migrations.AlterField(
            model_name='detallesproducto',
            name='color',
            field=models.CharField(choices=[('Gris', 'Gris'), ('Beige', 'Beige'), ('Verde', 'Verde'), ('Otros', 'Otro'), ('Amarillo', 'Amarillo'), ('Rojo', 'Rojo'), ('Rosado', 'Rosado'), ('Blanco', 'Blanco'), ('Marron', 'Marrón'), ('Negro', ' Negro'), ('Morado', 'Morado'), ('Azul', 'Azul'), ('Naranja', 'Naranja')], max_length=64),
        ),
        migrations.AlterField(
            model_name='detallesproducto',
            name='talla',
            field=models.CharField(choices=[('XL', 'xl'), ('S', 's'), ('L', 'l'), ('M', 'm'), ('XS', 'xs')], max_length=32),
        ),
    ]
