from asset_tracker.models import (
    User,
)
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "name": "testcase",
            "email": "testcase@example.com",
            "password": "testpass123",
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LoginTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(name="example",
                                            email='test@example.com',
                                            password="testpass123")

    def test_login(self):
        data = {
            "email": "test@example.com",
            "password": "testpass123"
        }
        response = self.client.post(reverse('token_obtain_pair'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)