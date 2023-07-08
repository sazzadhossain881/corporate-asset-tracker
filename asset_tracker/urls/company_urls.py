"""url mapping for the company api view"""
from django.urls import path
from asset_tracker.views import company_views as views


urlpatterns = [
    path('', views.CompanyListCreateView.as_view(), name='company-list-create'),
    path('<str:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),
]
