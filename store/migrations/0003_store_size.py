# Generated by Django 3.1 on 2020-11-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20201021_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='size',
            field=models.CharField(default=' × ', max_length=20),
        ),
    ]