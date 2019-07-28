# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dmodel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='dmodel',
            name='updated',
        ),
    ]
