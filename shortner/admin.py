from django.contrib import admin
from .models import ShortLink, Link

# Register your models here.
# admin.site.register(ShortLink)


class UrlAdmin(admin.ModelAdmin):
    list_display = ('shorten_link_path', 'source_link')

    def shorten_link_path(self, obj):
        return obj.short_url


admin.site.register(ShortLink, UrlAdmin)
admin.site.register(Link)
