from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models 

@admin.register(models.User)
class customUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "name",
                    "gender",
                    "birthday",
                    "password"
                ),
            },
        ),
    )
    list_display = (
        "name",
        "gender",
        "birthday",
    )
