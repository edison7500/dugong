# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-03 13:14
from __future__ import unicode_literals

import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Tutorial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=128, verbose_name="title"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.RandomCharField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        include_alpha=False,
                        length=12,
                        unique=True,
                    ),
                ),
                (
                    "status",
                    model_utils.fields.StatusField(
                        choices=[("draft", "draft"), ("published", "published")],
                        default="draft",
                        max_length=100,
                        no_check_for_status=True,
                        verbose_name="status",
                    ),
                ),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "origin_link",
                    models.URLField(
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="origin_link",
                    ),
                ),
                (
                    "created_datetime",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "published_at",
                    model_utils.fields.MonitorField(
                        default=django.utils.timezone.now,
                        monitor="status",
                        when=set(["published"]),
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tutorial",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "tutorial",
                "verbose_name_plural": "tutorial",
                "ordering": ["-published_at"],
            },
        )
    ]
