# Generated by Django 2.2.11 on 2020-03-18 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("photos", "0005_auto_20200317_1244")]

    operations = [migrations.RemoveField(model_name="photo", name="title")]
