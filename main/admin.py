from django.contrib import admin
from main.models import MenuContent, AboutContent

class AdminMenuContent(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']


class AboutPageContent(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']

# Register your models here.
admin.site.register(MenuContent, AdminMenuContent)
admin.site.register(AboutContent, AboutPageContent)