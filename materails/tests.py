from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from base.tests import BaseTestCase
from materails.models import Course, Lesson
from users.models import User


class MaterialsTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

        self.lesson = Lesson.objects.create(
            course=self.course,
            title='first test lesson',
            description='first test lesson description',
            video_link='first video link test',
            owner=self.user
        )

    def test_lesson_create(self):
        """ Создание урока """
        data_for_request = {
            'course': self.course.pk,
            'title': 'test lesson',
            'description': 'test lesson description',
            'video_link': 'video link test'
        }

        response = self.client.post(
            reverse('materials:create'),
            data_for_request
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_get_object(self):
        """ Получение одного урока """
        response = self.client.get(
            reverse('materials:read', args=[self.lesson.pk])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        expected_data = {
            'pk': self.lesson.pk,
            'course': self.lesson.course.pk,
            'title': self.lesson.title,
            'description': self.lesson.description,
            'video_link': self.lesson.video_link
        }

        self.assertEqual(
            response.json(),
            expected_data
        )

    def test_lesson_update(self):
        """ Редактирование урока """
        data_for_request = {
            'title': 'new title for lesson'
        }

        response = self.client.patch(
            reverse('materials:update', args=[self.lesson.pk]),
            data_for_request
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()
        self.assertEqual(
            self.lesson.title,
            data_for_request['title']
        )

