# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-17 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_shapeddata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shapeddata',
            name='degree',
        ),
        migrations.AddField(
            model_name='shapeddata',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]