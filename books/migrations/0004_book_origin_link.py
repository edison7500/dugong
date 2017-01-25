# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170125_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='origin_link',
            field=models.URLField(default=b'', max_length=255),
        ),
    ]
