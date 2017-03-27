# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0007_auto_20170327_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproject',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postproject',
            name='url',
            field=models.URLField(unique=True, max_length=255, blank=True),
        ),
    ]
