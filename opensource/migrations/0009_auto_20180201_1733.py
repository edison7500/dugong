# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import caching.base


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0008_auto_20180201_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, unique=True, blank=True)),
                ('bio', models.CharField(max_length=255, blank=True, null=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('organization', models.ForeignKey(blank=True, null=True, related_name='authors', to='opensource.Organization')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='author',
            name='organization',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
