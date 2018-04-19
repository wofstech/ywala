# Generated by Django 2.0.1 on 2018-03-10 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myhouses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_accomodation', models.CharField(max_length=200)),
                ('type_of_room', models.CharField(max_length=200)),
                ('house_rent', models.IntegerField()),
                ('availability', models.CharField(choices=[('A', 'Available'), ('NA', 'Not_Available')], default='A', max_length=2)),
                ('location', models.CharField(max_length=200)),
                ('nearest_institution', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='profile_image')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
