
from django.db import models
from devices.models import Device

class PowerEvent(models.Model):
    STATUS_CHOICES = (
        ("ON", "ON"),
        ("OFF", "OFF"),
    )

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="events")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.device_uid} - {self.status}"


