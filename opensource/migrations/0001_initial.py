# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import caching.base
import django.utils.timezone
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=128, unique=True, blank=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, unique=True, null=True)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='PostProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.URLField(max_length=255, unique=True, blank=True)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='opensource.Category')),
            ],
            options={
                'db_table': 'post_project',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('github_url', models.URLField(max_length=255, default='')),
                ('readme', django_markdown.models.MarkdownField(blank=True, null=True)),
                ('created_datetime', models.DateTimeField(db_index=True, auto_now=True)),
                ('display', models.BooleanField(default=True)),
                ('identified_code', models.CharField(max_length=32, unique=True, blank=True, null=True)),
                ('category', models.ForeignKey(null=True, related_name='category', to='opensource.Category')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('watch', models.PositiveIntegerField(default=0)),
                ('star', models.PositiveIntegerField(default=0)),
                ('fork', models.PositiveIntegerField(default=0)),
                ('datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('project', models.ForeignKey(related_name='github_status', to='opensource.Project')),
            ],
            options={
                'ordering': ('-datetime',),
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
    ]
