# Generated by Django 2.2.14 on 2020-11-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0002_opin_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opin',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]