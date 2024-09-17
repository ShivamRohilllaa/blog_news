from django.contrib import admin
from unfold.admin import ModelAdmin
from post.models import Blog, Category, Comment, SocialMedia, WebAddress

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'is_featured', 'is_latest', 'is_trending', 'created_at')
    list_filter = ('is_published', 'is_featured', 'is_latest', 'is_trending', 'category', 'created_at')
    search_fields = ('title', 'author__username', 'content', 'seo_title', 'seo_description', 'seo_keywords')
    prepopulated_fields = {"seo_slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'description')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('name', 'blog', 'content', 'created_at')
    search_fields = ('name', 'blog__title', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

class SocialMediaAdmin(ModelAdmin):
    # Specify fields to display in the admin list view
    list_display = ('facebook', 'twitter', 'instagram', 'gmail')

    # Search functionality to filter based on specific fields
    search_fields = ('facebook', 'twitter', 'instagram', 'gmail')

    # Optionally, make some fields read-only
    readonly_fields = ('id',)

# Register the model with the custom admin interface
admin.site.register(SocialMedia, SocialMediaAdmin)

class AddressAdmin(ModelAdmin):
    # Specify fields to display in the admin list view
    list_display = ('address_1', 'address_2', 'address_3', 'city', 'state', 'zipcode')

    # Search functionality to filter based on address fields
    search_fields = ('address_1', 'city', 'state', 'zipcode')

    # Optionally, make some fields read-only
    # readonly_fields = ('about',)

    # Optional: Group fields into sections in the admin form
    fieldsets = (
        (None, {
            'fields': ('address_1', 'address_2', 'address_3')
        }),
        ('Location Details', {
            'fields': ('state', 'city', 'zipcode')
        }),
        ('About', {
            'fields': ('about',)
        }),
    )

# Register the model with the custom admin interface
admin.site.register(WebAddress, AddressAdmin)