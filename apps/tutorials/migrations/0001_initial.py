# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
import tagging.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=128, blank=True)),
                ('slug', django_extensions.db.fields.RandomCharField(unique=True, blank=True, db_index=True, editable=False, length=12, include_alpha=False)),
                ('status', model_utils.fields.StatusField(verbose_name='status', max_length=100, default='draft', choices=[('draft', 'draft'), ('published', 'published')], no_check_for_status=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('origin_link', models.URLField(max_length=255, unique=True, null=True)),
                ('created_datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when=set(['published']))),
                ('tags', tagging.fields.TagField(max_length=255, blank=True)),
                ('author', models.ForeignKey(default=1, related_name='tutorial', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
                'ordering': ['-published_at'],
            },
        ),
        # migrations.CreateModel(
        #     name='TutorialImage',
        #     fields=[
        #         ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
        #         ('image', models.ImageField(upload_to=utils.image.handlers.UUIDFilename('tutorial/images/'))),
        #         ('is_cover', models.BooleanField(default=False)),
        #         ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
        #         ('post', models.ForeignKey(related_name='images', to='tutorials.Tutorial')),
        #     ],
        #     options={
        #         'db_table': 'tutorials_image',
        #         'ordering': ('-is_cover',),
        #     },
        # ),
    ]
