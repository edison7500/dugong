# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('source', models.CharField(default=b'', max_length=255, null=True)),
                ('buy_link', models.URLField(max_length=255, editable=False)),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('book', models.ForeignKey(related_name='images', to='books.Book')),
            ],
        ),
    ]
