# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0003_auto_20170326_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='identified_code',
            field=models.CharField(max_length=32, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='fork',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='star',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='status',
            name='watch',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
