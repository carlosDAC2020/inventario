from django.contrib import admin
from .models import Category, Product, Bill, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'company']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'Units_available', 'price_by_unit', 'category', 'company']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['description', 'expedition_date', 'company', 'administrator', 'total_price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'products_units', 'total_price', 'company', 'administrator', 'type']
