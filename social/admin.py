from django.contrib import admin
from social.models import Post


class PostAdmin(admin.ModelAdmin):
    
    list_display = ['content', 'author', 'created', 'last_updated']

admin.site.register(Post, PostAdmin)
