from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "email",
        "date_of_birth",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "username",
        "email",
        "date_of_birth",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "date_of_birth", "password")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "date_of_birth",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = (
        "username",
        "email",
        "date_of_birth",
    )
    ordering = (
        "username",
        "email",
        "date_of_birth",
    )


admin.site.register(CustomUser, CustomUserAdmin)
