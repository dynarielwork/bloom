

from django.contrib import admin

from .models import Category, Product, ProductImage, ProductReview

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'key_features', 'price', 'description']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
