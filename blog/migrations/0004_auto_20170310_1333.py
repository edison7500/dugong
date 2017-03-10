# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170117_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date', db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last_update', db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=1, verbose_name='status', choices=[(0, 'block'), (1, 'preview'), (2, 'publish')]),
        ),
    ]
