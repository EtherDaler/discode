# Generated by Django 3.2.1 on 2021-05-09 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_auto_20210509_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category', verbose_name='Лого'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 35, 28, 447041), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 35, 28, 447041), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 35, 28, 447041), verbose_name='Дата создания'),
        ),
    ]