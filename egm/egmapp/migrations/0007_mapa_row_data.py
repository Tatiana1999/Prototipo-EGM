# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('egmapp', '0006_remove_row_data_contenido2'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapa',
            name='Row_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='egmapp.Row_data'),
        ),
    ]
