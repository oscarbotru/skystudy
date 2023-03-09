import requests
from django.conf import settings
from rest_framework import status

from users.models import Payment


def get_payment_link(user, course):
    course_amount = int(course.price * 100)

    payment_item = Payment.objects.create(
        user=user,
        course=course,
        amount=course_amount,
        pay_type=Payment.PAY_TYPE_CARD
    )

    data_for_request = {
        "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
        "Amount": course_amount,
        "OrderId": f"{payment_item.pk}",
        "Description": f"Покупка курса {course.title}",
        "DATA": {
            "Email": user.email
        },
        "Receipt": {
            "Email": user.email,
            "Taxation": "usn_income",
            "Items": [
                {
                    "Name": course.title,
                    "Price": course_amount,
                    "Quantity": 1.00,
                    "Amount": course_amount,
                    "PaymentMethod": "full_prepayment",
                    "PaymentObject": "commodity",
                    "Tax": "vat10",
                    "Ean13": "0123456789"
                }
            ]
        }
    }

    response = requests.post(
        f'{settings.TINKOFF_URL}Init',
        json=data_for_request
    )

    if response.status_code == status.HTTP_200_OK:
        response_json = response.json()

        if response_json.get('Success'):
            payment_item.payment_id = response_json.get('PaymentId')
            payment_item.payment_url = response_json.get('PaymentURL')
            payment_item.save()

            return payment_item.payment_url

    return None
