# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0004_auto_20170327_0155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AddField(
            model_name='project',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]
