# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0022_auto_20160929_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='resposta',
        ),
        migrations.AddField(
            model_name='respostacomentarios',
            name='comentario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eventos.Comentarios'),
            preserve_default=False,
        ),
    ]
