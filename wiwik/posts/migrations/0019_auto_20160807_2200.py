# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_userprofile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='wiwiker',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]