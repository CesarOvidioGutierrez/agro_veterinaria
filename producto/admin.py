from django.contrib import admin
from .models import Product, Category, Brand, Supplier

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 10

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    list_per_page = 10

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'website')
    search_fields = ('name', 'address', 'phone', 'email', 'website')
    list_per_page = 10

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Supplier, SupplierAdmin)