# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0027_eventos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
    ]
