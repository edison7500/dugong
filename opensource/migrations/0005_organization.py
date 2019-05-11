# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import caching.base
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0004_auto_20180201_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('location', models.CharField(max_length=255, blank=True, null=True)),
                ('web_site', models.CharField(max_length=255, blank=True, null=True)),
                ('email', models.EmailField(max_length=255, blank=True, null=True)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organization',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]
