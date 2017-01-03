# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', redactor.fields.RedactorField(verbose_name='Text')),
                ('status', models.IntegerField(default=1, choices=[(0, 'block'), (1, 'preview'), (2, 'publish')])),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
