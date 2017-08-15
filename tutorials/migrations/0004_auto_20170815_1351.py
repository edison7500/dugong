# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20170815_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='updated_datetime',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([b'published']), monitor=b'status'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='status',
            field=model_utils.fields.StatusField(default=b'draft', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
    ]
