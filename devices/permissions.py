from rest_framework.permissions import BasePermission
from devices.models import Device

class IsAuthenticatedDevice(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Device)
