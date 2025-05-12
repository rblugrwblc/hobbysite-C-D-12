from user_management.models import Profile 
from django.db import models
from django.urls import reverse

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = "Thread Category"
        verbose_name_plural = "Thread Categories"  

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='threads')
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null = True, related_name='threads')
    entry = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:detail_view', args=[str(self.id)])
    

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='forum_comments')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        author_name = self.author.user.username if self.author and self.author.user else "Unknown"
        return f"{author_name}: {self.entry[:50]}{'...' if len(self.entry) > 50 else ''}"
