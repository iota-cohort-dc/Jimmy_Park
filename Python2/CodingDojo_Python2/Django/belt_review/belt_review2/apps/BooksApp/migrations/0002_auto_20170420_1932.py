# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='comments',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='ratings',
        ),
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
