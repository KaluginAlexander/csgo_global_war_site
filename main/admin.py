from django.contrib import admin
from main.models import MenuContent

class AdminMenuContent(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']

# Register your models here.
admin.site.register(MenuContent, AdminMenuContent)