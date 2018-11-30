from django.contrib import admin

# Register your models here.

from .models import UserProfile

class  UserProfileadmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileadmin)
