# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0023_auto_20160929_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respostacomentarios',
            name='comentario',
        ),
        migrations.AddField(
            model_name='comentarios',
            name='resposta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.RespostaComentarios'),
        ),
    ]
