from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name",
                    "last_name", 'get_photo', "is_staff", "is_active",
                    "date_joined")
    list_display_links = ("id", "username", "email")
    list_filter = ("date_joined", "is_staff", "is_active")
    search_fields = ("email", "date_joined")
    fields = ('username', 'email', 'first_name', 'last_name', 'get_photo', 'image',
              'is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('email', 'get_photo',)

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=80 alt='?'")
        else:
            return mark_safe("<img src='Photo/default/default_user_image.svg' width=80 alt='?'")

    get_photo.short_description = "user_photo"
