# Generated by Django 4.0.5 on 2022-07-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0018_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imgproductos'),
        ),
    ]