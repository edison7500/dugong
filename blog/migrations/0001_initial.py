# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from markdownx.models import MarkdownxField
import caching.base
# import django_markdown.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('slug', models.SlugField(max_length=30, unique=True, default='', editable=False)),
                ('content', MarkdownxField()),
                ('status', models.IntegerField(verbose_name='status', default=1, choices=[(0, 'block'), (1, 'preview'), (2, 'publish')])),
                ('created_date', models.DateTimeField(verbose_name='created_date', db_index=True, auto_now_add=True)),
                ('last_update', models.DateTimeField(verbose_name='last_update', db_index=True, auto_now=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='post/images')),
                ('uploaded_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(related_name='images', to='blog.Post')),
            ],
        ),
    ]
