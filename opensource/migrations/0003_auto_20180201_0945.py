# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0002_auto_20180131_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='created_datetime',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
