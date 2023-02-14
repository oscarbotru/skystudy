from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=128, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
