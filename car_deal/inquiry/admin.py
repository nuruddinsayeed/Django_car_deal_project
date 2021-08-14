from inquiry.models import Inquiry
from django.contrib import admin


class InqueiryAdmin(admin.ModelAdmin):
    """Customize inquiry for the admin page display"""

    list_display = ("id", "name", "car", "created_at")
    list_display_links = ("id", "name", "car")
    search_fields = ("name",)
    list_per_page = 25
    list_filter = ("car", )


admin.site.register(Inquiry, InqueiryAdmin)
