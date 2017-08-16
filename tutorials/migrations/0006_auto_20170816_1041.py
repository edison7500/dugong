# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import model_utils.fields
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_auto_20170815_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tags',
            field=tagging.fields.TagField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='status',
            field=model_utils.fields.StatusField(default=b'draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title', blank=True),
        ),
    ]
