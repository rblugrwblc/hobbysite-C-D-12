from django.contrib import admin
from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'people_required', 'created_on', 'updated_on')
    search_fields = ('title', 'description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commission', 'created_on')
    search_fields = ('entry',)

admin.site.register(Commission)
admin.site.register(Comment)
# Register your models here.
