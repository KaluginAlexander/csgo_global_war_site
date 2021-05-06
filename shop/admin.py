from django.contrib import admin
from shop.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subscription', 'cost', 'amount']
    list_display_links = ['id', 'title']


admin.site.register(Product, ProductAdmin)