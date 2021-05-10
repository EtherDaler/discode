# Generated by Django 3.2.1 on 2021-05-06 12:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('body', models.TextField(blank=True, verbose_name='Описание')),
                ('discount', models.PositiveIntegerField(blank=True, default=0, verbose_name='Скидка')),
                ('slug', models.SlugField(max_length=200, verbose_name='Код')),
                ('date_of_create', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 43, 11, 184939), verbose_name='Дата создания')),
                ('date_of_finish', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 43, 11, 184939), verbose_name='Дата окончания')),
                ('active', models.BooleanField(blank=True, default=False, verbose_name='Активность')),
                ('watch', models.PositiveIntegerField(blank=True, default=0, verbose_name='Просмотров')),
            ],
            options={
                'verbose_name': 'События (акции, скидки)',
                'verbose_name_plural': 'События (акции, скидки)',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='discounts/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фотографии',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('logo', models.ImageField(blank=True, upload_to='brand_logo', verbose_name='Лого')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка на партнера')),
            ],
            options={
                'verbose_name': 'Партнеры',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255, verbose_name='Объект акции/скидки')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.discounts', verbose_name='Акция')),
            ],
            options={
                'verbose_name': 'Объекты акиций/скидок',
                'verbose_name_plural': 'Объекты акиций/скидок',
            },
        ),
    ]