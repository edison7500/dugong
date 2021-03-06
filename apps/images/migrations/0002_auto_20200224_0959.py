# Generated by Django 2.2.10 on 2020-02-24 01:59

import apps.images.handlers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("images", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={
                "ordering": ["-uploaded_at"],
                "verbose_name": "image",
                "verbose_name_plural": "image",
            },
        ),
        migrations.AddField(
            model_name="image",
            name="height",
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name="image",
            name="width",
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name="image",
            name="file",
            field=models.ImageField(
                height_field="height",
                upload_to=apps.images.handlers.UUIDFilename("images/"),
                width_field="width",
            ),
        ),
    ]
