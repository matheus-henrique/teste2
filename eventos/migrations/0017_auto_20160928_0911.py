# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0016_auto_20160928_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evt', to='eventos.Eventos'),
        ),
    ]
