import secrets
from django.db import models
from houses.models import House

class Device(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name="devices")
    device_uid = models.CharField(max_length=50, unique=True)
    api_key = models.CharField(max_length=64, unique=True)
    last_seen = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = secrets.token_hex(32)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.device_uid

