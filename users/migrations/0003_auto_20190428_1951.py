# Generated by Django 2.2 on 2019-04-28 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190428_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
        migrations.AddField(
            model_name='user',
            name='campus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Campus'),
        ),
        migrations.AddField(
            model_name='user',
            name='schoolo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.School'),
        ),
    ]
