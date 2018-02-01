# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0003_auto_20180201_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created',
        ),
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
