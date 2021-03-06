# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kalyan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50, unique=True)),
                ('num_suggestions', models.IntegerField()),
                ('num_complains', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Complains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('complain_for', models.CharField(max_length=50)),
                ('ucomplain', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('many_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyan.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('feed', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('suggest_for', models.CharField(max_length=50)),
                ('usuggestion', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('many_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyan.Category')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_logged_in',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='suggestions',
            name='many_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyan.Profile'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='many_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyan.Profile'),
        ),
        migrations.AddField(
            model_name='complains',
            name='many_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kalyan.Profile'),
        ),
    ]
