# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='username',
        ),
    ]
