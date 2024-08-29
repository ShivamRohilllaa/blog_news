from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    blog_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)

    # SEO Fields
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_description = models.CharField(max_length=160, blank=True, null=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)
    seo_slug = models.SlugField(max_length=255, unique=True)
    canonical_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate SEO title and slug if not provided
        if not self.seo_title:
            self.seo_title = self.title
        if not self.seo_slug:
            self.seo_slug = self.title.lower().replace(' ', '-')
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
