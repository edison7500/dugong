# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0005_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='bio',
            field=models.CharField(max_length=255, blank=True, default=''),
        ),
    ]
