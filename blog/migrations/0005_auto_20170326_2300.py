# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170310_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
