# Generated by Django 4.0.4 on 2022-06-21 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipos_completos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='area',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='descripcion_equipo',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='componente',
            new_name='ds_efecto_modo_falla',
        ),
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='componente_pauta',
            new_name='ds_modo_falla',
        ),
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='criticidad',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='equiposcompletos',
            old_name='equipo_principal',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='lazo_control',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='numero_equipo',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='sistema',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='sub_sistema',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='tag_componente',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='tag_equipo',
        ),
        migrations.RemoveField(
            model_name='equiposcompletos',
            name='ubicacion_tecnica',
        ),
        migrations.AddField(
            model_name='equiposcompletos',
            name='descripcion_tarea',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
