from django.contrib import admin
from .models import Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'show_text', 'created_date']
    list_display_links = ['id', 'post', 'user', 'show_text', 'created_date']
    ordering = ['created_date']

    def show_text(self, obj):
        return obj.text.split('.')[0]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'image', 'show_content', 'publish', 'created', 'updated', 'status']
    list_display_links = ['id', 'title', 'slug', 'image', 'show_content', 'publish', 'created', 'updated', 'status']
    search_fields = ['id', 'title', 'slug']
    ordering = ['created', 'status']

    def show_content(self, obj):
        return obj.content.split('.')[0]


