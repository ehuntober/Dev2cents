import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Cent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cents")
    description = models.TextField(null=True)
    hearts = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.owner} -- {self.description}"


class Like(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="likes")
    cent = models.ForeignKey(Cent, on_delete=models.CASCADE, null=True, related_name="likes")
    already_liked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.owner} -- {self.cent}"
