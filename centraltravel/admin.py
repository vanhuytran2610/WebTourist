from django.contrib import admin
from .models import Post_Central

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'upload_to']
    list_filter = ['upload_to']
    search_fields = ['title']
admin.site.register(Post_Central, PostAdmin)