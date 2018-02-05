# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0013_auto_20180205_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=128, default='')),
                ('name', models.CharField(max_length=128, default='')),
                ('desc', models.TextField(blank=True, null=True)),
                ('readme', models.TextField(blank=True, null=True)),
                ('url', models.URLField(max_length=255, blank=True, null=True)),
                ('identified_code', models.CharField(max_length=32, unique=True, blank=True, null=True)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
