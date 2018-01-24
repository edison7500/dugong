# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0010_auto_20170801_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.URLField(max_length=255, default=''),
        ),
    ]
