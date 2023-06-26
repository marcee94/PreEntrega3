# Generated by Django 4.2.2 on 2023-06-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratorio', models.CharField(max_length=30)),
                ('operario', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('equipo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('resultado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('institucion', models.CharField(max_length=30)),
                ('informe', models.CharField(max_length=30)),
                ('mamografia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
