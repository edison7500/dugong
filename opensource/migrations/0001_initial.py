# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, unique=True, null=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(default=b'', max_length=255, blank=True)),
                ('name', models.CharField(default=b'', max_length=255, blank=True)),
                ('desc', models.TextField(null=True, blank=True)),
                ('github_url', models.URLField(default=b'', max_length=255)),
                ('readme', django_markdown.models.MarkdownField(null=True, blank=True)),
                ('created_datetime', models.DateTimeField(auto_now=True, db_index=True)),
                ('category', models.ForeignKey(related_name='category', to='opensource.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watch', models.PositiveIntegerField(default=0, editable=False)),
                ('star', models.PositiveIntegerField(default=0, editable=False)),
                ('fork', models.PositiveIntegerField(default=0, editable=False)),
                ('project', models.ForeignKey(related_name='github_project', to='opensource.Project')),
            ],
        ),
    ]
