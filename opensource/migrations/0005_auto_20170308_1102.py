# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0004_auto_20170306_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github_url',
            field=models.URLField(default=b'', max_length=255),
        ),
    ]
