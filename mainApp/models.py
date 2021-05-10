from django.db import models
from myAuth.models import User
from datetime import date
import datetime
import re
from django.template.defaultfilters import slugify

def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):

    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)

def _slug_strip(value, separator='-'):
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


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
	partner = models.ForeignKey(Partner, on_delete = models.CASCADE, verbose_name = 'Партнер')
	name = models.CharField(max_length = 255, verbose_name = 'Название')
	body = models.TextField(blank=True, verbose_name = "Описание")
	discount = models.PositiveIntegerField(default = 0, blank = True, verbose_name = 'Скидка')
	slug = models.SlugField(max_length=200, db_index=True, verbose_name = "Код")
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Категория', blank = True, related_name = 'discounts')
	date_of_create = models.DateTimeField(verbose_name = 'Дата создания', default = default_datetime(), blank = True)
	date_of_finish = models.DateTimeField(verbose_name = 'Дата окончания', default = default_datetime(), blank = True)
	active = models.BooleanField(verbose_name = 'Активность', default = False, blank = True)
	watch = models.PositiveIntegerField(default = 0, blank = True, verbose_name = 'Просмотров')

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



