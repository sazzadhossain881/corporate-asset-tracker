"""url mapping for the device api view"""
from django.urls import path
from asset_tracker.views import device_views as views


urlpatterns = [
    path('', views.DeviceListCreateView.as_view(), name='device-list-create'),
    path('<str:pk>/', views.DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('assign/create/', views.DeviceAssignCreateView.as_view(), name='device-assign-create'),
    path('<str:pk>/assign/', views.DeviceAssignUpdateView.as_view(), name='device-assign-update'),
]
