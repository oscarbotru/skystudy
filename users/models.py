from django.conf import settings
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


class Payment(models.Model):
    PAY_TYPE_CARD = 'card'
    PAY_TYPE_CASH = 'cash'

    PAY_TYPES = (
        (PAY_TYPE_CASH, 'наличные'),
        (PAY_TYPE_CARD, 'перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь',
                             on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name='дата оплаты', **NULLABLE)

    lesson = models.ForeignKey('materails.Lesson', on_delete=models.CASCADE,
                               verbose_name='урок', **NULLABLE)
    course = models.ForeignKey('materails.Course', on_delete=models.CASCADE,
                               verbose_name='курс', **NULLABLE)

    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='сумма оплаты')
    pay_type = models.CharField(choices=PAY_TYPES, default=PAY_TYPE_CASH, max_length=10,
                                verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.amount}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('materails.Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
