from django.urls import path
from .views import DevicePowerEventView, UserPowerEventsView

urlpatterns = [
    path("device/power/", DevicePowerEventView.as_view(), name="device_power_event"),
    path("power-events/", UserPowerEventsView.as_view(), name="user_power_events"),
]