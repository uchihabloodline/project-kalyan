# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalyan', '0011_auto_20170815_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.BooleanField(default=False),
        ),
    ]
