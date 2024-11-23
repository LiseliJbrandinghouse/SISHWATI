from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Allows admin to add images for multiple colors

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_new_arrival', 'created_at', 'is_out_of_stock')
    list_filter = ('category', 'is_new_arrival', 'created_at', 'is_out_of_stock', 'is_new_collection')
    inlines = [ProductImageInline]
    search_fields = ('name',)

