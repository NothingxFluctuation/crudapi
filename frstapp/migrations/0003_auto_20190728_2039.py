# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frstapp', '0002_auto_20190728_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmodel',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
