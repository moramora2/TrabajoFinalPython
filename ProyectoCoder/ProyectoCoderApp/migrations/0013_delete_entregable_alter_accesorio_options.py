# Generated by Django 4.0.5 on 2022-07-15 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0012_delete_curso_delete_estudiante_delete_profesor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.AlterModelOptions(
            name='accesorio',
            options={},
        ),
    ]