"""Test for models"""
from asset_tracker import models

from django.test import TestCase
from django.contrib.auth import get_user_model


def create_user(email='user@example.com',name='Test Name', password='testpass123'):
    """create and return a new user"""
    return get_user_model().objects.create_user(email,name, password)


class TestModels(TestCase):
    """Test models"""

    def test_create_user_with_email_successfull(self):
        """Test creating a user with email is success"""
        email = 'test@example.com'
        name='Test Name'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email if normalized for new user"""
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises as ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Test Name',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_company(self):
        """Test creating a company is successfull"""
        company = models.Company.objects.create(
            name='Test Name',
            location='test location',
            phone_number='01727265079'
        )
        self.assertEqual(str(company), company.name)

    def test_create_device(self):
        """Test create device is successfull"""
        company = models.Company.objects.create(
            name='Test Name',
            location='test location',
            phone_number='01727265079'
        )
        device = models.Device.objects.create(
            name='Test Name',
            description='sample description',
            serial_number='s017272650',
            condition='Good',
            checked_out=False,
            company=company
        )
        self.assertEqual(str(device), device.name)