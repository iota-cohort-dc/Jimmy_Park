# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='interest',
        ),
        migrations.AddField(
            model_name='users',
            name='userInterest',
            field=models.ManyToManyField(related_name='user_interest', to='Interest.Interests'),
        ),
    ]
