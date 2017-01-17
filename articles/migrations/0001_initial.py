# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, blank=True)),
                ('slug', models.SlugField()),
                ('content', redactor.fields.RedactorField(verbose_name='Text')),
                ('status', models.PositiveSmallIntegerField(default=1, choices=[(0, 'block'), (1, 'draft'), (2, 'publish')])),
                ('created_datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, blank=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='category', to='articles.Category'),
        ),
    ]
