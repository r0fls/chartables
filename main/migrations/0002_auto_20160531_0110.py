# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
