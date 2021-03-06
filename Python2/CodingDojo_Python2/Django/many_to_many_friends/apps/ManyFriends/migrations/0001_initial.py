# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friend', to='ManyFriends.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_name', to='ManyFriends.User'),
        ),
    ]
