# Generated by Django 2.0.1 on 2018-05-16 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_auto_20180312_0520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myhouses',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='myhouses',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
