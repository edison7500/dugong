# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0007_author_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='avatar',
            field=models.URLField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
