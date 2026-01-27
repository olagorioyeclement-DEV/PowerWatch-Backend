from rest_framework import serializers
from .models import PowerEvent

class PowerEventSerializer(serializers.ModelSerializer):
    device_uid = serializers.CharField(
        source="device.device_uid",
        read_only=True
    )

    class Meta:
        model = PowerEvent
        fields = [
            "device_uid",
            "power",
            "status",
            "timestamp",
        ]

