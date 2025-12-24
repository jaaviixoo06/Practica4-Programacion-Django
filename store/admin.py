from django.contrib import admin
from .models import Seller, Customer, Product, Order, OrderItem

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'user')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'stock', 'category')
    prepopulated_fields = {'slug': ('name',)}

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('price',)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]
