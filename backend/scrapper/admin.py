from django.contrib import admin

from .models import Data, Site

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ("text", )
    list_filter = ('created', 'updated',)

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("url", "name", "status", "created", "updated")
    list_filter = ("name", "status", "created", "updated")