# Generated by Django 3.2.1 on 2021-05-06 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email адресс')),
                ('phone', models.CharField(max_length=255, unique=True, verbose_name='Телефон')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('number_of_uses', models.PositiveIntegerField(default=0, verbose_name='Количество использованных купонов')),
                ('subscribe', models.BooleanField(default=False)),
                ('client', models.BooleanField(default=True)),
                ('partner', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date_of_register', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 43, 11, 182922), null=True, verbose_name='Дата регистрации')),
                ('last_visit', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 6, 17, 43, 11, 182922), verbose_name='Последняя активность')),
                ('login_count', models.PositiveIntegerField(blank=True, default=1, verbose_name='Количество входов на сайт')),
                ('edit_count', models.PositiveIntegerField(blank=True, default=1, verbose_name='Количество редактирований профиля')),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователей',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
