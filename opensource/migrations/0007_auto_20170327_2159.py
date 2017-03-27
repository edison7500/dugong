# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0006_auto_20170327_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
