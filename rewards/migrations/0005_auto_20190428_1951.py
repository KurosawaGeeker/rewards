# Generated by Django 2.2 on 2019-04-28 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0004_auto_20190428_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 19, 51, 56, 238697), verbose_name='date published'),
        ),
    ]