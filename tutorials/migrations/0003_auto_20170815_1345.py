# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_tutorial_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=django_extensions.db.fields.RandomCharField(editable=False, include_alpha=False, length=12, blank=True, unique=True, db_index=True),
        ),
    ]
