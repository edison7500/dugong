# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0015_auto_20180205_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='url',
            field=models.URLField(max_length=255, unique=True, default=''),
        ),
    ]
