# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-24 06:09
from __future__ import unicode_literals

import apps.images.handlers
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=apps.images.handlers.UUIDFilename('images/'))),
                ('description', models.CharField(blank=True, max_length=255)),
                ('is_cover', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'db_table': 'generic_image',
                'abstract': False,
            },
        ),
    ]
