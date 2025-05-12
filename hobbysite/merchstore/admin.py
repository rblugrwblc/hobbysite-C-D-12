from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, ProductType, Product, Transaction

class ProfileInline(admin.StackedInline):
        model = Profile
        can_delete = False

class UserAdmin(admin.ModelAdmin):
        inlines = [ProfileInline,]

class ProductTypeAdmin(admin.ModelAdmin):
        model = ProductType

        list_display = ('name',)
        list_filter = ('name',)

class ProductAdmin(admin.ModelAdmin):
	model = Product

	list_display = ('name', 'product_type', 'price')
	list_filter = ('name', 'product_type',)

class TransactionAdmin(admin.ModelAdmin):
        model = Transaction

        list_display = ('buyer__name', 'product__name', 'amount', 'status')


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
