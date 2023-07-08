"""url mapping for the employee api view"""
from django.urls import path
from asset_tracker.views import employee_views as views


urlpatterns = [
    path('', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('<str:pk>/', views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('<str:pk>/assignments/', views.EmployeeAssignmentsListView.as_view(), name='employee-assignments-list'),
]

