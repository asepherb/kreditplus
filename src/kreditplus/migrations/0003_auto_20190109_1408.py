# Generated by Django 2.1.5 on 2019-01-09 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kreditplus', '0002_auto_20190109_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formapplication',
            name='birthdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
