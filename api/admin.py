from django.contrib import admin

# Register your models here.
from .models.ProfileModel import Profile
admin.site.register(Profile)
