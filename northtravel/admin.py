from django.contrib import admin
from .models import Post_North

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'upload_to']
    list_filter = ['upload_to']
    search_fields = ['title']
admin.site.register(Post_North, PostAdmin)
