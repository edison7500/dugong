# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0011_auto_20180201_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='nickname',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='url',
            field=models.URLField(max_length=255, blank=True, null=True),
        ),
    ]
