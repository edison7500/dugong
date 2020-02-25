# Generated by Django 2.2.10 on 2020-02-25 09:20

import apps.images.handlers
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('description', models.TextField(blank=True, default='')),
                ('file', models.ImageField(height_field='height', upload_to=apps.images.handlers.hexdigest_filename, width_field='width')),
                ('width', models.IntegerField(default=0, editable=False)),
                ('height', models.IntegerField(default=0, editable=False)),
                ('uploaded_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='Exif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('photo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exif', to='photos.Photo')),
            ],
        ),
    ]