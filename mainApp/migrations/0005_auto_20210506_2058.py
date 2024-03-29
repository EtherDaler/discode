# Generated by Django 3.2.1 on 2021-05-06 15:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0004_auto_20210506_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 20, 58, 53, 356649), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 20, 58, 53, 356649), verbose_name='Дата окончания'),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Название организации/компании')),
                ('info', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(blank=True, max_length=18, verbose_name='Телефон')),
                ('site', models.CharField(max_length=255, verbose_name='Ссылка на сайт')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
        ),
    ]
