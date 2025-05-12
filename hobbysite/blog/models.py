from django.db import models
from django.urls import reverse
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
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='articles')
    category = models.ForeignKey(ArticleCategory,
                                 null=True,
                                 blank=True, 
                                 on_delete=models.SET_NULL)
    entry = models.TextField() 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    header_image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail_view", args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Article, 
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='forum_comments')
    entry = models.TextField() 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

class ArticleGallery(models.Model):
    article_gallery = models.ImageField(upload_to='images/', null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'images')

    def __str__(self):
        return f'Image for {self.article.title}'
   
