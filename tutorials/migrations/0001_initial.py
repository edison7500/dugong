# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('content', models.TextField()),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
