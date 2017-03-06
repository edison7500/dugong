# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('github_url', models.URLField(default=b'')),
                ('readme', django_markdown.models.MarkdownField()),
                ('stat', models.PositiveIntegerField(default=0)),
                ('updated_datetime', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
