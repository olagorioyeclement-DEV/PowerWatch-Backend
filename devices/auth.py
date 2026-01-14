from rest_framework.permissions import BasePermission
from devices.models import Device

class IsAuthenticatedDevice(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get("X-API-KEY")
        if not api_key:
            return False
        return Device.objects.filter(api_key=api_key).exists()
