from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from devices.auth import DeviceAPIKeyAuthentication
from .models import PowerEvent
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PowerEventSerializer
from devices.auth import DeviceAPIKeyAuthentication
from devices.permissions import IsAuthenticatedDevice

class DevicePowerEventView(APIView):
    authentication_classes = [DeviceAPIKeyAuthentication]
    permission_classes = [IsAuthenticatedDevice]

    def post(self, request):
        device = request.user  # ✅ Authenticated Device

        status = request.data.get("status")
        if status not in ["ON", "OFF"]:
            return Response({"error": "Invalid status"}, status=400)

        PowerEvent.objects.create(device=device, status=status)

        device.last_seen = timezone.now()
        device.save()

        return Response({"message": "Power event recorded"})


class UserPowerEventsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PowerEventSerializer

    def get_queryset(self):
        return PowerEvent.objects.filter(
            device__house__user=self.request.user
        ).order_by("-timestamp")

