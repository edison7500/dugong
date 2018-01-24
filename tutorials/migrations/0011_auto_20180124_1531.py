# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import utils.image.handlers
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0010_auto_20171018_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when=set(['published'])),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='status',
            field=model_utils.fields.StatusField(verbose_name='status', max_length=100, default='draft', choices=[(0, 'dummy')], no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='tutorialimage',
            name='image',
            field=models.ImageField(upload_to=utils.image.handlers.UUIDFilename('tutorial/images/')),
        ),
    ]
