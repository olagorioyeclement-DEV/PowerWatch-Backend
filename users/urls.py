from django.urls import path
from .views import (
    SignUpView, LoginView,
    HouseCreateView, HouseListView,
    DeviceCreateView, DeviceListView,
    HouseDetailView,
)

urlpatterns = [
    # User auth
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    # Houses
    path('houses/', HouseListView.as_view(), name='house-list'),
    path('houses/create/', HouseCreateView.as_view(), name='house-create'),
    path('houses/<int:pk>/', HouseDetailView.as_view(), name='house-detail'),

    # Devices
    path('devices/', DeviceListView.as_view(), name='device-list'),
    path('devices/create/', DeviceCreateView.as_view(), name='device-create'),
]
