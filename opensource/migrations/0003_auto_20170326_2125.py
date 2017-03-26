# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0002_auto_20170326_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='identified_code',
            field=models.CharField(max_length=64, unique=True, null=True, blank=True),
        ),
    ]
