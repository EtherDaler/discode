# Generated by Django 3.2.1 on 2021-05-06 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20210506_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requests',
            options={'verbose_name': 'Запросы на партнерство', 'verbose_name_plural': 'Запросы на партнерство'},
        ),
        migrations.AddField(
            model_name='requests',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 21, 16, 34, 134282), verbose_name='Дата запроса'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 21, 16, 34, 133297), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 21, 16, 34, 133297), verbose_name='Дата окончания'),
        ),
    ]