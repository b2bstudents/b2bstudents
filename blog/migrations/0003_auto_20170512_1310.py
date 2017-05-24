# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='docfile',
            field=models.FileField(default='Images/0.jpg', upload_to='Images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de publication'),
        ),
    ]
