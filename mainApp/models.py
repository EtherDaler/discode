from django.db import models
from myAuth.models import User

import datetime
from ckeditor.fields import RichTextField


def default_datetime(): 
    return datetime.datetime.now()


class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True, verbose_name = "Название")
    image = models.ImageField(upload_to = 'category', verbose_name = 'Лого', blank = True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name = "Код") # используется для получения уникального URL пути

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Partner(models.Model):
	owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Владелец', related_name = 'company')
	name = models.CharField(max_length = 255, verbose_name = 'Название')
	inn = models.PositiveIntegerField(verbose_name = 'ИНН', default = 0)
	contact_face = models.CharField(max_length = 255, verbose_name = 'контактное лицо', default = ' ')
	phone = models.CharField(max_length = 255, verbose_name = 'Телефон (основной)', default = ' ')
	adress = models.CharField(max_length = 255, verbose_name = 'Адресс', default = ' ')
	email = models.CharField(max_length = 255, verbose_name = 'Email', default = ' ')
	logo = models.ImageField(upload_to = 'brand_logo', verbose_name = 'Лого', blank = True) # нужно лого загружать по сортированным папкам
	link = models.CharField(max_length = 255, verbose_name = 'Ссылка на партнера')
	instagram = models.CharField(max_length = 255, verbose_name = 'Ссылка на instagram', blank = True)
	facebook = models.CharField(max_length = 255, verbose_name = 'Ссылка на facebook', blank = True)
	linkedin = models.CharField(max_length = 255, verbose_name = 'Ссылка на linkedin', blank = True)
	active = models.BooleanField(default = False, blank = True, verbose_name = 'Прошел проверку модератором/администратором')
	date_of_create = models.DateTimeField(verbose_name = 'Дата создания', default = default_datetime(), blank = True)

	class Meta:
		verbose_name = 'Партнеры'
		verbose_name_plural = 'Партнеры'

	def __str__(self):
		return self.name

class Felials(models.Model):
	partner = models.ForeignKey(Partner, on_delete = models.CASCADE, verbose_name = 'Партнер', related_name = 'felials')
	adress = models.CharField(max_length = 255, verbose_name = 'Адресс', blank = True)

	class Meta:
		verbose_name = 'Фелиалы'
		verbose_name_plural = 'Фелиалы'

	def __str__(self):
		return self.adress

class AnotherPhones(models.Model):
	partner = models.ForeignKey(Partner, on_delete = models.CASCADE, related_name = 'another_phones', verbose_name = 'Партнер')
	phone = models.CharField(max_length = 255, verbose_name = 'Телефон', blank = True)

	class Meta:
		verbose_name = 'Другие номера'
		verbose_name_plural = 'Другие номера'

	def __str__(self):
		return self.phone

class Discounts(models.Model):
	partner = models.ForeignKey(Partner, on_delete = models.CASCADE, verbose_name = 'Партнер', related_name = 'discounts')
	name = models.CharField(max_length = 255, verbose_name = 'Название')
	body = models.TextField(blank=True, verbose_name = "Описание")
	discount = models.PositiveIntegerField(default = 0, blank = True, verbose_name = 'Скидка')
	slug = models.SlugField(max_length=200, db_index=True, verbose_name = "Код")
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Категория', blank = True, related_name = 'discounts')
	date_of_create = models.DateTimeField(verbose_name = 'Дата создания', default = default_datetime(), blank = True)
	date_of_finish = models.DateTimeField(verbose_name = 'Дата окончания', default = default_datetime(), blank = True)
	active = models.BooleanField(verbose_name = 'Активность', default = False, blank = True)
	watch = models.PositiveIntegerField(default = 0, blank = True, verbose_name = 'Просмотров')

	def watch_up(self):
		self.watch += 1
		return self.watch

	class Meta:
		verbose_name = 'События (акции, скидки)'
		verbose_name_plural = 'События (акции, скидки)'

	def __str__(self):
		return "Название: {}, id: {}".format(self.name, self.id)

class Images(models.Model):
	discount = models.ForeignKey(Discounts, on_delete = models.CASCADE, verbose_name = 'Акция', related_name = 'images')
	image = models.ImageField(upload_to='discounts/%Y/%m/%d', blank=True, verbose_name = "Фото")

	class Meta:
		verbose_name = 'Фотографии'
		verbose_name_plural = 'Фотографии'

	def __str__(self):
		return '{}: {}'.format(self.discount, self.image)

class Products(models.Model):
	discount = models.ForeignKey(Discounts, on_delete = models.CASCADE, verbose_name = 'Акция', related_name = 'products')
	product = models.CharField(max_length = 255, verbose_name = 'Объект акции/скидки', blank=True)

	class Meta:
		verbose_name = 'Объекты акиций/скидок'
		verbose_name_plural = 'Объекты акиций/скидок'

	def __str__(self):
		return '{}:{}'.format(self.discount, self.product)

class News(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	body = models.TextField(verbose_name="Текст сообщения", blank=True)
	html = models.FileField(upload_to='email/html/%Y/%m/%d', verbose_name='HTML-файл', blank=True)
	date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

	class Meta:
		verbose_name = 'Рассылки'
		verbose_name_plural = 'Рассылки'

	def __str__(self):
		return self.title

class Newsletter(models.Model):
	email = models.CharField(max_length = 255, verbose_name = 'Email', blank=True)
	date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

	class Meta:
		verbose_name = 'Подписчики на рассылку'
		verbose_name_plural = 'Подписчики на рассылку'

	def __str__(self):
		return self.email

class Blog(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	body = RichTextField(verbose_name='Текст блога')
	main_image = models.ImageField(upload_to='blog_logo/%Y/%m/%d', verbose_name='Обложка')
	date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Блоги'
		verbose_name_plural = 'Блоги'

	def __str__(self):
		return '{} {}'.format(self.title, self.date)
		

class Events(models.Model):
	blog = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = 'Блог', blank=True)
	image = models.ImageField(upload_to='carusel/%Y/%m/%d', blank=True, verbose_name = "Фото")
	button_color = models.CharField(max_length=255, verbose_name='Цвет кнопки в хеш', blank=True)
	button_href = models.CharField(max_length=255, verbose_name='Ссылка на кнопке', blank=True)
	button_text = models.CharField(max_length = 255, verbose_name = 'Надпись на кнопке')
	active = models.BooleanField(default=False, verbose_name='Активность')

	class Meta:
		verbose_name = 'События'
		verbose_name_plural = 'События'

	def __str__(self):
		return self.id

class Comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='comments')
	discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, verbose_name='Акция/скидка', related_name='comments')
	answer = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Ответ')
	rating = models.PositiveIntegerField(default=0, verbose_name='Оценка')
	text = models.TextField(verbose_name='Текст')
	rating_used = models.BooleanField(default=False, verbose_name='Поставил оценку')
	active = models.BooleanField(default=False, verbose_name='Активность')
	date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Комментарии'
		verbose_name_plural = 'Комментарии'

	def __str__(self):
		return 'Пользователь {} написал кооментарий к {}. Статус: {}'.format(self.user, self.discount.name, self.active)


