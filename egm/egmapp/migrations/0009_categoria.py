# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egmapp', '0008_remove_mapa_row_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.IntegerField()),
            ],
        ),
    ]
