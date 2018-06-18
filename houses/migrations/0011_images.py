# Generated by Django 2.0.1 on 2018-06-11 13:04

from django.db import migrations, models
import django.db.models.deletion
import houses.models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0010_auto_20180611_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('myhouses', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='houses.Myhouses')),
            ],
        ),
    ]
