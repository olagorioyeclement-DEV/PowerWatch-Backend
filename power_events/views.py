from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from devices.models import Device
from devices.auth import IsAuthenticatedDevice
from rest_framework.generics import ListAPIView
from .models import PowerEvent
from .serializers import PowerEventSerializer

class DevicePowerEventView(APIView):
    permission_classes = [IsAuthenticatedDevice]

    def post(self, request):
        api_key = request.headers.get("X-API-KEY")
        device = Device.objects.get(api_key=api_key)

        status = request.data.get("status")
        if status not in ["ON", "OFF"]:
            return Response({"error": "Invalid status"}, status=400)

        PowerEvent.objects.create(device=device, status=status)
        device.last_seen = timezone.now()
        device.save()

        return Response({"message": "Power event recorded"})

class UserPowerEventsView(ListAPIView):
    permission_classes = [IsAuthenticatedDevice]
    serializer_class = PowerEventSerializer

    def get_queryset(self):
        return PowerEvent.objects.filter(
            device__house__user=self.request.user
        ).order_by("-timestamp")

