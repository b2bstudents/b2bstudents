# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='pseudo',
            field=models.CharField(max_length=42),
        ),
    ]
