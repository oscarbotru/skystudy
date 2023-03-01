from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from base.tests import BaseTestCase
from materails.models import Course, Lesson
from users.models import User, Subscription


class SubscriptionTestCase(BaseTestCase):

    def _send_subscription_request(self):
        self.client.post(
            '/users/subscribe/',
            {
                'course': self.course.pk
            }
        )

    def test_subscription(self):
        """ Подписка """
        queryset = Subscription.objects.filter(
            user=self.user,
            course=self.course
        )

        self._send_subscription_request()

        self.assertTrue(queryset.exists())

        self._send_subscription_request()

        self.assertFalse(queryset.exists())
