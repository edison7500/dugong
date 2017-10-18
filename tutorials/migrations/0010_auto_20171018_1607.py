# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.image.handlers


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_auto_20170819_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorialimage',
            options={'ordering': ('-is_cover',)},
        ),
        migrations.AddField(
            model_name='tutorialimage',
            name='is_cover',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tutorialimage',
            name='image',
            field=models.ImageField(upload_to=utils.image.handlers.UUIDFilename(b'tutorial/images/')),
        ),
    ]
