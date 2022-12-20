from django.contrib import admin
from django.contrib import admin
from . import models 

@admin.register(models.Book)
class customUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "title",
                    "spend_cate",
                    "money",
                    "spend_date",
                    "bio",
                    "user",
                ),
            },
        ),
    )
    list_display = (
        "title",
        "spend_cate",
        "money",
    )
