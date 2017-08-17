# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20170817_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'post/images')),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(related_name='images', to='tutorials.Tutorial')),
            ],
            options={
                'db_table': 'tutorials_image',
            },
        ),
    ]
