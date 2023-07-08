from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.conf import settings
from django.core.validators import RegexValidator
import re

# Create your models here.
class UserProfileManager(BaseUserManager):
    """manager for user profile"""
    def create_user(self, email, name, password=None):
        """create, save and return a new user"""
        if not email:
            raise ValueError('user must have an email address')
        user = self.model(email = self.normalize_email(email),name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and return a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        """retrieve short name of the user"""
        return self.name

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def __str__(self):
        """string representation of the user"""
        return self.email


class Company(models.Model):
    """Company objects"""
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']
        db_table = 'company'

    def __str__(self):
        return self.name


class Device(models.Model):
    """Device objects"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.CharField(max_length=255, default='Good')
    checked_out = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['serial_number']
        db_table = 'Device'

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Employee objects"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         null=True
         )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, through='DeviceAssignment')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['user']
        db_table = 'Employee'

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class DeviceAssignment(models.Model):
    """DeviceAssignment objects"""
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'DeviceAssignment'
        verbose_name_plural = 'DeviceAssignment'
        ordering = ['-updated_at']  # from top to bottom
        db_table = 'DeviceAssignment'

    def __str__(self):
        if self.return_date:
            return f"{self.device.name} returned by {self.employee.user.get_username()} at: ({self.return_date.ctime()})"
        return f"{self.device.name} assigned to {self.employee.user.get_username()}, at: ({self.assigned_date.ctime()})"

