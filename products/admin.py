from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'description',
        'image',
        'category',
    )


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
