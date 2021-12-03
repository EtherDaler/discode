# Generated by Django 3.2.1 on 2021-05-16 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_auto_20210516_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Подписчики на рассылку', 'verbose_name_plural': 'Подписчики на рассылку'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 21, 42, 18, 742724), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 21, 42, 18, 742724), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 21, 42, 18, 742724), verbose_name='Дата создания'),
        ),
    ]
