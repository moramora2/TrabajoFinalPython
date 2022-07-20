# Generated by Django 4.0.5 on 2022-07-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0030_accesorio_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idvehiculo', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('comentario', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
