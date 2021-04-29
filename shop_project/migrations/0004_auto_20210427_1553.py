# Generated by Django 3.1.2 on 2021-04-27 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_project', '0003_auto_20210427_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='create_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(),
        ),
    ]