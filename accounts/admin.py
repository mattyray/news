from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "age", "is_staff", "bio"]

    # Fieldsets for editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "bio", "profile_picture")}),  # Including all custom fields
    )

    # Fieldsets for creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", "bio", "profile_picture")}),  # Ensure custom fields are included
    )


admin.site.register(CustomUser, CustomUserAdmin)
