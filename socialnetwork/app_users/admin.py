from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick_name', 'name', 'last_name', 'birthday', 'email', 'phone_number', 'country', 'city']



