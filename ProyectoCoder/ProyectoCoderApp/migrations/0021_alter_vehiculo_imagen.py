# Generated by Django 4.0.5 on 2022-07-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0020_alter_vehiculo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/imgproductos'),
        ),
    ]
