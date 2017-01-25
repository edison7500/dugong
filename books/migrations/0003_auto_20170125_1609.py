# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170125_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='brief',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='origin_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='price',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='source',
        ),
        migrations.AddField(
            model_name='book',
            name='asin',
            field=models.CharField(default=b'', max_length=255, editable=False),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=b'book/images/'),
        ),
    ]
