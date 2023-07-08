"""serializer for the user api view"""
from rest_framework import serializers
from asset_tracker import models
from rest_framework_simplejwt.tokens import RefreshToken

from asset_tracker.models import (
    User,
    Company,
    Employee,
    Device,
    DeviceAssignment,
)


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user"""
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'isAdmin', 'token']
        extra_kwargs = {
            'token': {
                'read_only': True,
            }
        }

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class CompanySerializer(serializers.ModelSerializer):
    """serializer for the company objects"""
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    """serializer for the device objects"""
    class Meta:
        model = Device
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """serializer for the employee objects"""
    class Meta:
        model = Employee
        fields = '__all__'


class DeviceAssignmentSerializer(serializers.ModelSerializer):
    """serializer for deviceAssignment objects"""
    # device = DeviceSerializer(read_only=True)
    # employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceAssignment
        fields = '__all__'

