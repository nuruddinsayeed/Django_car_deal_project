from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    """Customize team view in admin page"""

    def thumbnil(self, object):
        """This will recieve model data as object here
        So we will retrieve photo from it and retrun as html <IMG/>
        and also this thumbnil will be availabel as obj attribute"""

        return format_html(
            '<img src="{}" width="40" style="border-radius: 50px;"/>'.format(
                object.photo.url  # this will be available inside src{}
            )
        )

    def name(self, object):
        "return full name"
        return (object)

    # lest change thumnil title(description) from thumb-> photo
    thumbnil.short_description = "photo"

    list_display = ('id', 'thumbnil', 'name',
                    'designation', 'created_at',)
    list_display_links = ('id', 'thumbnil', 'name',)
    # now lets create a search filds for the admin panel
    search_fields = ('first_name', 'last_name', 'designation',)
    # lets create filter option for the admin panel
    list_filter = ('designation', )


admin.site.register(Team, TeamAdmin)
