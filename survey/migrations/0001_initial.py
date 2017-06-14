# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-10 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefToken',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('token', models.CharField(max_length=255)),
                ('yes', models.IntegerField()),
                ('no', models.IntegerField()),
            ],
        ),
    ]
