# Generated by Django 2.2.14 on 2020-11-24 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0006_auto_20201123_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opin',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='opin',
            name='not_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
