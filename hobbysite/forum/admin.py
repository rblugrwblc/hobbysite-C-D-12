from django.contrib import admin
from .models import Post, PostCategory

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

    search_fields = ('name', )

class PostAdmin(admin.ModelAdmin):
    model = Post

    search_fields = ('name', )
    list_display = ('title', 'category', 'created_on',)
    list_filter = ('category',)

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
