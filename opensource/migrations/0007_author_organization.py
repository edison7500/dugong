# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensource', '0006_organization_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, related_name='authors', to='opensource.Organization'),
        ),
    ]
