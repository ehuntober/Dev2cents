import uuid

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=25, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["created"]
        verbose_name_plural = 'Categories'


class Cent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cents")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cents')
    description = RichTextField(config_name="awesome_ckeditor", null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner} -- {self.description}"

    class Meta:
        ordering = ["created"]
