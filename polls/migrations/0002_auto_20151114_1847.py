# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='capcity',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='course_section',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(default=None, max_length=2, choices=[(b'Le', b'Lecture'), (b'La', b'Lab'), (b'Q', b'Quiz')]),
        ),
        migrations.AddField(
            model_name='course',
            name='days',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='course',
            name='registered',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='polls.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=None, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')]),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(default=None, max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior'), (b'GR', b'Graduate')]),
        ),
    ]
