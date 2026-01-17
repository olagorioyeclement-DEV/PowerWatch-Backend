from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from devices.models import Device

class DeviceAPIKeyAuthentication(BaseAuthentication):
    keyword = "Api-Key"

    def authenticate(self, request):
        auth = request.headers.get("Authorization")

        if not auth:
            return None

        if not auth.startswith(self.keyword + " "):
            return None

        api_key = auth.split(" ", 1)[1]

        try:
            device = Device.objects.get(api_key=api_key, is_active=True)
        except Device.DoesNotExist:
            raise AuthenticationFailed("Invalid device API key")

        return (device, None)

