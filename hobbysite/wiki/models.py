from django.db import models
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Article Categories"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    
    author = models.ForeignKey(
        Profile, 
        null=True, 
        on_delete=models.SET_NULL
    )
    
    category = models.ForeignKey(
        ArticleCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    entry = models.TextField()
    header_image = models.ImageField(upload_to='articles/headers/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"