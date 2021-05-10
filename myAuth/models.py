from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from datetime import date
import datetime

def default_datetime(): 
    return datetime.datetime.now()

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone = phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            password=password,
            phone = phone,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email адресс',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length = 255, verbose_name = "Телефон", unique = True)
    first_name = models.CharField(max_length = 255, blank = True, verbose_name = "Имя")
    number_of_uses = models.PositiveIntegerField(default = 0, verbose_name = "Количество использованных купонов")
    subscribe = models.BooleanField(default = False, verbose_name = 'Подписка')
    client = models.BooleanField(default = True, verbose_name = 'Пользователь')
    partner = models.BooleanField(default = False, verbose_name = 'Партнер')
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    date_of_register = models.DateTimeField(default=default_datetime(), null=True, blank = True, verbose_name = 'Дата регистрации')
    last_visit = models.DateTimeField(verbose_name='Последняя активность', default=default_datetime(), blank = True)
    login_count = models.PositiveIntegerField(verbose_name='Количество входов на сайт', default=1, blank = True)
    edit_count = models.PositiveIntegerField(verbose_name='Количество редактирований профиля', default=1, blank = True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    #REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Пользователей'
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.admin and self.is_active

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.admin and self.is_active

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.staff

    def is_partner(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.partner

    def is_client(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.client

    def can_use(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.subscribe and self.number_of_uses < 10

    @property
    def is_admin(self):
        "Is the user a member of admins?"
        # Simplest possible answer: All admins are staff
        return self.admin

    """
    def get_full_name(self):
    	return '%s %s' % (self.first_name, self.last_name)
	"""
	
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
    	self.edit_count += 1
    	super().save()

