# Generated by Django 4.0.4 on 2022-06-14 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maquina', '0001_initial'),
        ('fmeca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmeca',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fmeca_list', to='maquina.maquina'),
        ),
    ]
