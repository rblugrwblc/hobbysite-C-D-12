from django.db import models
from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Product(models.Model):
    status_options = [
        ('Available', 'Available'),
        ('On Sale', 'On Sale'),
        ('Out of Stock', 'Out of Stock'),
    ]
    
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    stock = models.IntegerField(default=1)
    status = models.CharField(choices=status_options, default="Available")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.status = "Out of Stock"
            self.stock = 0
        else:
            self.status = "Available" if self.status == "Out of Stock" else self.status
        super().save(*args, **kwargs)

class Transaction(models.Model):
    status_options = [
        ('On cart', 'On cart'),
        ('To Pay', 'To Pay'),
        ('To Ship', 'To Ship'),
        ('To Receive', 'To Receive'),
        ('Delivered', 'Delivered'),
    ]
    
    buyer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(default=1)
    status = models.CharField(null=True, choices=status_options)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.buyer.name
