from datetime import datetime

from django.core.management import BaseCommand

from materails.models import Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = []
        for user in User.objects.all():
            for i in range(10):
                payment_list.append(
                    Payment(
                        user=user,
                        datetime=datetime.now(),
                        lesson=Lesson.objects.all().order_by('?').first(),
                        amount=1000,
                        pay_type=Payment.PAY_TYPE_CARD
                    )
                )

        Payment.objects.bulk_create(payment_list)
