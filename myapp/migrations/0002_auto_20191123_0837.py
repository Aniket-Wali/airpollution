# Generated by Django 2.2.5 on 2019-11-23 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='air_quality_cities',
            name='Category_of_ES',
        ),
        migrations.RemoveField(
            model_name='air_quality_cities',
            name='Type',
        ),
    ]
