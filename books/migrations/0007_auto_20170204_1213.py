# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170202_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
