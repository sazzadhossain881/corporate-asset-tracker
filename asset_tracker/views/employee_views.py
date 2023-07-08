"""views for the employee api"""
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from asset_tracker.models import (
    Employee,
)
from asset_tracker.serializers import (
    EmployeeSerializer,
    DeviceAssignmentSerializer,
)

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class EmployeeAssignmentsListView(generics.ListAPIView):
    serializer_class = DeviceAssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return DeviceAssignment.objects.filter(employee=employee_id)
