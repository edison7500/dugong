# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0010_auto_20180201_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='url',
        ),
        migrations.AddField(
            model_name='people',
            name='avatar',
            field=models.URLField(max_length=255, blank=True, null=True),
        ),
    ]
