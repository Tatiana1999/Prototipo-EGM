# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('egmapp', '0019_mapa_codigos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapa',
            old_name='Codigos',
            new_name='preguntas',
        ),
    ]
