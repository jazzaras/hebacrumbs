# Generated by Django 2.2.14 on 2020-11-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0003_auto_20201123_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opin',
            name='pub_date',
            field=models.DateTimeField(default='0000-00-00', null=True),
        ),
    ]
