from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'balance', 'price']
    list_filter = ['category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'balance', 'price']
    list_display_links = ['pk']

# Register your models here.
admin.site.register(Product, ProductAdmin)