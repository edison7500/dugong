# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170326_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'post/images')),
                ('uploaded_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(related_name='images', to='blog.Post')),
            ],
        ),
    ]
