from django.contrib import admin
from users.models import Profile, Newsletter
# Register your models here.


admin.site.register([Profile, Newsletter])
