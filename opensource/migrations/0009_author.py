# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import caching.base


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0008_auto_20170327_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=128, blank=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]
