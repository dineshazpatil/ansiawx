# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_v330_custom_venv_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiedjob',
            name='controller_node',
            field=models.TextField(blank=True, default='', editable=False, help_text='The instance that managed the isolated execution environment.'),
        ),
    ]
