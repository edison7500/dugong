# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0009_auto_20180201_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'people', 'verbose_name_plural': 'people'},
        ),
        migrations.RemoveField(
            model_name='people',
            name='organization',
        ),
        migrations.AddField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='location',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='web_site',
            field=models.URLField(max_length=255, blank=True, null=True),
        ),
    ]
