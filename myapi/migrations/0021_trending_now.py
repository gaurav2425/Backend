# Generated by Django 3.1.7 on 2021-03-01 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0020_trending_dateint'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='now',
            field=models.CharField(default='', max_length=20, verbose_name=datetime.datetime(2021, 3, 1, 10, 30, 50, 73382, tzinfo=utc)),
        ),
    ]
