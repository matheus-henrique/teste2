# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-11 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0035_notifications_lido'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='num_participantes',
            field=models.IntegerField(default=0),
        ),
    ]
