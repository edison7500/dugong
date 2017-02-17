# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20170204_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='book',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
