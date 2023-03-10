import datetime

import pytz
from django.conf import settings
from django.db import models
from materails.tasks import send_notify_update
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course_preview/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='стоимость')

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if self.pk is not None:
            now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
            if (now - self.updated_at).seconds > 4 * 60 * 60:
                send_notify_update.delay(self.pk)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course_preview/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    video_link = models.CharField(max_length=255, verbose_name='видео')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title} ({self.course.title})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
