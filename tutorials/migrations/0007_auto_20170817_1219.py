# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20170816_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ['-published_at'], 'verbose_name': '\u6559\u7a0b', 'verbose_name_plural': '\u6559\u7a0b'},
        ),
        migrations.AddField(
            model_name='tutorial',
            name='origin_link',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
