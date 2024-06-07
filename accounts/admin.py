from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm #specifries the form to use or changing an existing user
    model = CustomUser          #specifies the form to use for creating a new ujser
    list_display = [ #displays view in admin panel
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),) #inherits the default fieldsets from UserAdmin
    #also adds age for the fieldset for changing a current user user
    add_fieldsets = UserAdmin.add_fieldsets + ( 
        (
            None,
            {"fields": ("age",)} #adds fieldset for creating a new user
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
