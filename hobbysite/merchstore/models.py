from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)
    email = models.EmailField()

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Transaction(models.Model):
    buyer = models.ForgeignKey(Profile, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    status = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)
