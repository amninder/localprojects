# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 05:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20170611_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='refquestion',
            options={'ordering': ('title',)},
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
