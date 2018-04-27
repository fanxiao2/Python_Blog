# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-27 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_at']},
        ),
        migrations.AddField(
            model_name='article',
            name='reading',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
