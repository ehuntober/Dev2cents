import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Cent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cents")
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} -- {self.description}"

    class Meta:
        ordering = ["created"]
