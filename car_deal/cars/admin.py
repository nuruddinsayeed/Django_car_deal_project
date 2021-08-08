from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    """Customize Car model in admin page"""

    def thumbnil(self, object):
        """Create icon for car obj"""

        return format_html(
            '<img src={} width="40" style="border-radius: 6px;"/>'
            .format(object.car_photo.url)
        )

    # Change thumbnil title to Car's Image
    thumbnil.short_descripiton = "Car's Image"
    list_display = ('id', 'thumbnil', 'car_title', 'city', 'model', 'year',
                    'body_style', 'fuel_type', 'is_featured', 'created_date',)
    list_display_links = ('id', 'thumbnil', 'car_title',)
    list_editable = ('is_featured',)

    # add Search Filed at the top of car model admin page
    search_fields = ('id', 'car_title', 'city', 'model', 'fuel_type',)
    list_filter = ('city', 'body_style', 'fuel_type',)


admin.site.register(Car, CarAdmin)
