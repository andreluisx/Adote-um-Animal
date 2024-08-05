from django.contrib import admin

# Register your models here.
from .models import User, ProfileImage

admin.site.register(User)
admin.site.register(ProfileImage)
