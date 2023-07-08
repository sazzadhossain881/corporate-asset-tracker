"""views for the device api"""
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from asset_tracker.serializers import (
    DeviceSerializer,
    DeviceAssignmentSerializer
)
from asset_tracker.models import (
    Device,
    DeviceAssignment,
)

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DeviceAssignCreateView(generics.CreateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DeviceAssignUpdateView(generics.UpdateAPIView):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
