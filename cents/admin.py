from django.contrib import admin
from cents.models import Cent, Like

# Register your models here.

admin.site.register([Cent, Like])