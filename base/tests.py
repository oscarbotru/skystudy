from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materails.models import Course, Lesson
from users.models import User, Subscription


class BaseTestCase(APITestCase):
    email = 'test@test.com'
    password = '123qwe456rty'

    def setUp(self) -> None:
        self.user = User.objects.create(
            email=self.email
        )
        self.user.set_password(self.password)
        self.user.save()

        response = self.client.post(
            '/users/token/',
            {
                'email': self.email,
                'password': self.password
            }
        )

        self.token = response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.course = Course.objects.create(title='test course')
