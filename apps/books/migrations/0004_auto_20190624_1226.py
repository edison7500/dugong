# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='download_link',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
    ]