# Generated by Django 2.2 on 2019-04-21 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 21, 20, 25, 46, 582763), verbose_name='date published'),
        ),
    ]