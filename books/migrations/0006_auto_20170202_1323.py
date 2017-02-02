# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20170126_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='asin',
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]
