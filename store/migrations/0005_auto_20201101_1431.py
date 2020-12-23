# Generated by Django 3.1 on 2020-11-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_store_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='price',
            new_name='price0',
        ),
        migrations.RemoveField(
            model_name='store',
            name='size',
        ),
        migrations.AddField(
            model_name='store',
            name='size0',
            field=models.CharField(default='', max_length=20),
        ),
    ]