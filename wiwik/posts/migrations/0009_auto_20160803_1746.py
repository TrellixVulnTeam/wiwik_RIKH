# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20160803_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_comments',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
