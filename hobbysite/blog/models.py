from datetime import datetime
from django.db import models

class Article_Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Article Categories"

    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Article_Category,null=True,blank=True, on_delete=models.SET_NULL)
    entry = models.TextField() 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
   
