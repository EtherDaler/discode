# Generated by Django 3.2.1 on 2021-05-06 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20210506_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 46, 25, 513048), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 46, 25, 513048), verbose_name='Дата окончания'),
        ),
    ]
