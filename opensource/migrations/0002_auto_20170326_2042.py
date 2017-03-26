# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='identified_code',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='project',
            field=models.ForeignKey(related_name='github_status', to='opensource.Project'),
        ),
    ]
