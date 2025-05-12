from django.contrib import admin
from .models import Thread, ThreadCategory, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

    search_fields = ('name', )

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    search_fields = ('name', )
    list_display = ('title', 'category', 'created_on',)
    list_filter = ('category',)
    inlines = [CommentInline]

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)