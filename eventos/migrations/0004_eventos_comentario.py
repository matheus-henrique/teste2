# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20160927_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='comentario',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
