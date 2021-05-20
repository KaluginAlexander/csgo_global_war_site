from django.contrib import admin
from main.models import MenuContent, AboutContent, Question

class AdminMenuContent(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']


class AboutPageContent(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    list_display = ['question']

# Register your models here.
admin.site.register(MenuContent, AdminMenuContent)
admin.site.register(AboutContent, AboutPageContent)
admin.site.register(Question, QuestionAdmin)