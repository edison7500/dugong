# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20170815_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
    ]
