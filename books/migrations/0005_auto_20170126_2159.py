# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_origin_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='asin',
            field=models.CharField(unique=True, max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
