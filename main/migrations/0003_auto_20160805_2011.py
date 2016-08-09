# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 20:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20160805_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary_contents',
            old_name='preparing_person',
            new_name='title',
        ),
        migrations.AddField(
            model_name='diary_contents',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]