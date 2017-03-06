# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0002_auto_20170306_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='fork',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='project',
            name='watch',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='readme',
            field=django_markdown.models.MarkdownField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='star',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
