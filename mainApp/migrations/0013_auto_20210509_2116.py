# Generated by Django 3.2.1 on 2021-05-09 16:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_auto_20210508_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='mainApp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 16, 7, 45023), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 16, 7, 45023), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 9, 21, 16, 7, 29403), verbose_name='Дата создания'),
        ),
    ]