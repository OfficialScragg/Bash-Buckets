# Generated by Django 3.2 on 2021-06-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BashBuckets', '0004_rename_userbuckets_userbucket'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usage_limit',
            field=models.IntegerField(default=1024),
        ),
    ]
