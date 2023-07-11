from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")
    list_display_links = ("id", "username", "email")
    list_filter = ("date_joined", "is_staff", "is_active")
    search_fields = ("email", "date_joined")
