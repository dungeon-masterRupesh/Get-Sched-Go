# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailystats',
            name='CompletedClassTiming',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailystats',
            name='CompletedExtraCurricularsTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailystats',
            name='CompletedExtraStudyTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailystats',
            name='CompletedMiscellaneousTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dailystats',
            name='CompletedSelfStudy',
            field=models.IntegerField(default=0),
        ),
    ]
