# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('source', models.CharField(default=b'', max_length=30)),
                ('origin_id', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='buy_link',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='source',
        ),
        migrations.AddField(
            model_name='book',
            name='brief',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='create_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='purchase',
            name='book',
            field=models.ForeignKey(related_name='purchases', to='books.Book'),
        ),
    ]
