# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-20 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liuyao', '0005_yao_reverse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liushen',
            fields=[
                ('rigan', models.CharField(max_length=250, primary_key='true', serialize=False)),
                ('liuyao', models.CharField(max_length=250)),
                ('wuyao', models.CharField(max_length=250)),
                ('siyao', models.CharField(max_length=250)),
                ('sanyao', models.CharField(max_length=250)),
                ('eryao', models.CharField(max_length=250)),
                ('chuyao', models.CharField(max_length=250)),
            ],
        ),
    ]