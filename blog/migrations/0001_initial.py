# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import caching.base
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(default=b'', unique=True, max_length=30, editable=False)),
                ('content', django_markdown.models.MarkdownField()),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'block'), (1, 'preview'), (2, 'publish')])),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created_date', db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last_update', db_index=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'post/images')),
                ('uploaded_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(related_name='images', to='blog.Post')),
            ],
        ),
    ]
