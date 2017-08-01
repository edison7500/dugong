# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0009_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.CharField(unique=True, max_length=128, blank=True),
        ),
    ]
