from django.db import models

class Commission(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commission = models.ForeignKey(
        Commission, 
        on_delete=models.CASCADE,
        related_name = 'comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment on {self.commission.title} at {self.created_on}'
