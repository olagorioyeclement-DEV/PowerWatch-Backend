from django.db import models
from users.models import User

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="houses")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

