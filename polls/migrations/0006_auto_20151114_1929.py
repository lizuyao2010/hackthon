# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151114_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='time',
        ),
        migrations.AddField(
            model_name='course',
            name='end_time',
            field=models.TimeField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_time',
            field=models.TimeField(default=True),
        ),
    ]
