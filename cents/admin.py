from django.contrib import admin
from cents.models import Cent, Category

# Register your models here.

admin.site.register([Cent, Category])