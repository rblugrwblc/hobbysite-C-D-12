from django.contrib import admin
from .models import ProductType, Product

# Register your models here.
class ProductTypeAdmin(admin.ModelAdmin):
	model = ProductType

	list_display = ('name',)
	list_filter = ('name',)

class ProductAdmin(admin.ModelAdmin):
	model = Product

	list_display = ('name', 'product_type', 'price')
	list_filter = ('name', 'product_type',)


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
