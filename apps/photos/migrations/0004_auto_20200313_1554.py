# Generated by Django 2.2.11 on 2020-03-13 07:54

import apps.images.handlers
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20200306_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AddField(
            model_name='exif',
            name='shot_time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.images.handlers.hexdigest_filename),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=apps.images.handlers.hexdigest_filename),
        ),
    ]
