# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='studyChoice',
            field=models.CharField(choices=[('1', 'Day'), ('2', 'Evening'), ('3', 'Night'), ('4', 'Late Night')], default='3', max_length=1),
        ),
    ]
