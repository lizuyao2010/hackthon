# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151114_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.FloatField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=True, max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.DurationField(default=True),
        ),
    ]
