# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0005_auto_20170327_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=255, blank=True)),
                ('category', models.ForeignKey(to='opensource.Category')),
            ],
            options={
                'db_table': 'post_project',
            },
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ('-datetime',)},
        ),
    ]
