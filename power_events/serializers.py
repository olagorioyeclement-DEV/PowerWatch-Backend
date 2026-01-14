from rest_framework import serializers
from .models import PowerEvent

class PowerEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerEvent
        fields = ["status"]

