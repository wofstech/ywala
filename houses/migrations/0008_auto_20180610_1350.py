# Generated by Django 2.0.1 on 2018-06-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_auto_20180610_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myhouses',
            name='type_of_apartment',
            field=models.CharField(choices=[('F', 'Flat'), ('s', 'Self_contained'), ('b', 'Bungalow'), ('s', 'Mini_flat'), ('D', 'Duplex')], max_length=2),
        ),
    ]