# Generated by Django 4.0.4 on 2022-06-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquiposCompletos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('tag_equipo', models.CharField(max_length=255)),
                ('equipo_principal', models.CharField(max_length=255)),
                ('sistema', models.CharField(max_length=255)),
                ('sub_sistema', models.CharField(max_length=255)),
                ('lazo_control', models.CharField(max_length=255)),
                ('tag_componente', models.CharField(max_length=255)),
                ('componente', models.CharField(max_length=255)),
                ('ubicacion_tecnica', models.CharField(max_length=255)),
                ('numero_equipo', models.CharField(max_length=255)),
                ('descripcion_equipo', models.TextField()),
                ('criticidad', models.CharField(max_length=255)),
                ('funcion_equipo', models.TextField()),
                ('falla_funcional', models.TextField()),
                ('componente_pauta', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
