# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0011_auto_20160927_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.Eventos'),
        ),
    ]