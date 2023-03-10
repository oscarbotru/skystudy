from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from users.models import Subscription


@shared_task
def send_notify_update(course_pk):
    course_list = Subscription.objects.filter(course_id=course_pk)
    for course_item in course_list:
        send_mail(
            subject=f'Обновление курса {course_item.course.title}',
            message=f'Обновление курса {course_item.course.title}',
            recipient_list=[course_item.user.email],
            from_email='admin@local.com'
        )
