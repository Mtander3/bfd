# Generated by Django 2.1.1 on 2018-10-03 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181003_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 11, 1, 12, 761940, tzinfo=utc)),
        ),
    ]
