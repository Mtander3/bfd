# Generated by Django 2.1.1 on 2018-10-03 10:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180922_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 10, 27, 28, 196285, tzinfo=utc)),
        ),
    ]
