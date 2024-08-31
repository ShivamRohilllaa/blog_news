from django.contrib import admin
from post.models import Blog, Category, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'is_featured', 'is_latest', 'is_trending', 'created_at')
    list_filter = ('is_published', 'is_featured', 'is_latest', 'is_trending', 'category', 'created_at')
    search_fields = ('title', 'author__username', 'content', 'seo_title', 'seo_description', 'seo_keywords')
    prepopulated_fields = {"seo_slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'content', 'created_at')
    search_fields = ('user__username', 'blog__title', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
