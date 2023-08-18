from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _
# import email_normalize
from users.validators import phone_validator


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def _create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('super_user', 'Директор'),
        ('admin', 'Админ'),
        ('seller', 'Продавец'),
        ('deliveryman', 'Доставщик'),
    )
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True)
    avatar = ResizedImageField(
        verbose_name="Изображение",
        size=(400, 400),
        blank=True, null=True,
        crop=['middle', 'center'],
        upload_to='users_avatar',
    )
    email = models.EmailField(verbose_name='Почта', unique=True, blank=True)
    username = models.CharField(verbose_name='Имя пользователя', max_length=255, unique=True)
    is_staff = models.BooleanField(verbose_name='Статус сотрудника', default=False, )
    is_active = models.BooleanField(verbose_name='Активен', default=True, )
    phone = models.CharField(verbose_name='Номер телефона', max_length=255, null=True, blank=False,
                             validators=[phone_validator, ])
    user_type = models.CharField(verbose_name='Тип пользователя', max_length=255, choices=USER_TYPE,
                                 default='seller',)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
