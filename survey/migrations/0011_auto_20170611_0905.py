# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20170611_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='token',
            name='yes',
            field=models.IntegerField(default=0),
        ),
    ]
