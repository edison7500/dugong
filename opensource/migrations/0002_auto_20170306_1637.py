# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='stat',
            new_name='star',
        ),
    ]
