# Generated by Django 3.1.2 on 2021-04-27 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_project', '0002_auto_20210426_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, default=datetime.datetime.now),
        ),
    ]