# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_tutorialimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='origin_link',
            field=models.URLField(max_length=255, unique=True, null=True),
        ),
    ]
