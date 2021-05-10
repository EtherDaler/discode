# Generated by Django 3.2.1 on 2021-05-06 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAuth', '0003_auto_20210506_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_register',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 20, 58, 53, 354649), null=True, verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_visit',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 20, 58, 53, 354649), verbose_name='Последняя активность'),
        ),
    ]
