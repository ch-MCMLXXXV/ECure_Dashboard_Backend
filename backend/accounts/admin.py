from django.contrib import admin

# Register your models hefrom django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import StaffCreationForm, StaffChangeForm
from .models import Staff


class StaffAdmin(UserAdmin):
    add_form = StaffCreationForm
    form = StaffChangeForm
    model = Staff
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    ordering = ("email",)


admin.site.register(Staff, StaffAdmin)
