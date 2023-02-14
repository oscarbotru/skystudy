from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course_preview/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course_preview/', **NULLABLE, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    video_link = models.CharField(max_length=255, verbose_name='видео')

    def __str__(self):
        return f'{self.title} ({self.course.title})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
