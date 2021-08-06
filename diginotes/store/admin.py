from django.contrib import admin
from .models import Product, Category, Payment, UserProduct

# Register your models here.
class productAdmin(admin.ModelAdmin):
    model = Product
    list_display=['name', 'category', 'price', 'discount', 'active']

admin.site.register(Category)
admin.site.register(Product, productAdmin)
admin.site.register(Payment)
admin.site.register(UserProduct)