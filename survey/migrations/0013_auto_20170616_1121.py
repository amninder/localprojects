# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_auto_20170613_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='no',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='token',
            name='yes',
        ),
    ]