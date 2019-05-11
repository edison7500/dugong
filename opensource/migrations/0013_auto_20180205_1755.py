# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0012_auto_20180203_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'people', 'verbose_name_plural': 'people', 'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=django_extensions.db.fields.RandomCharField(unique=True, blank=True, db_index=True, editable=False, length=12, include_alpha=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='url',
            field=models.URLField(max_length=255, unique=True, default=''),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
