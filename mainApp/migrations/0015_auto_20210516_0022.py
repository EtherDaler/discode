# Generated by Django 3.2.1 on 2021-05-16 00:22

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0014_auto_20210509_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Текст блога')),
                ('main_image', models.ImageField(upload_to='blog_logo/%Y/%m/%d', verbose_name='Обложка')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Блоги',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, verbose_name='Текст сообщения')),
                ('html', models.FileField(blank=True, upload_to='email/html/%Y/%m/%d', verbose_name='HTML-файл')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Рассылки',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Email')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Рассылки',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 0, 22, 28, 165509), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='date_of_finish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 0, 22, 28, 165509), verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='discounts',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='mainApp.partner', verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='date_of_create',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 16, 0, 22, 28, 165509), verbose_name='Дата создания'),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='carusel/%Y/%m/%d', verbose_name='Фото')),
                ('button_color', models.CharField(blank=True, max_length=255, verbose_name='Цвет кнопки в хеш')),
                ('button_href', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на кнопке')),
                ('button_text', models.CharField(max_length=255, verbose_name='Надпись на кнопке')),
                ('blog', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.blog', verbose_name='Блог')),
            ],
            options={
                'verbose_name': 'События',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting', models.PositiveIntegerField(default=0, verbose_name='Оценка')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('active', models.BooleanField(default=False, verbose_name='Активность')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.comments', verbose_name='Ответ')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.discounts', verbose_name='Акция/скидка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарии',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]