# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postproject',
            options={'verbose_name': 'post project', 'verbose_name_plural': 'post projects', 'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='postproject',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
