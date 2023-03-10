import requests
from celery import shared_task
from django.conf import settings

from users.models import Payment


@shared_task
def check_payment_status():
    payment_list = Payment.objects.filter(status__in=[Payment.STATUS_NEW, Payment.STATUS_HANDLE])
    for payment_item in payment_list:
        print('check payment status')
        # data_for_request = {...}
        # requests.post(
        #     f'{settings.TINKOFF_URL}getState',
        #     data_for_request
        # )
