# Generated by Django 3.2 on 2021-06-05 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BashBuckets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBuckets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BashBuckets.bucket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BashBuckets.bucket')),
            ],
        ),
    ]
