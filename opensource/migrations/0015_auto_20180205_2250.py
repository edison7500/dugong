# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0014_repository'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'verbose_name': 'repository', 'verbose_name_plural': 'repositories'},
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=128, blank=True, null=True),
        ),
    ]
