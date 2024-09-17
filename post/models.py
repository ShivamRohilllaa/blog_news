from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_top_three = models.BooleanField(default=False)
    sort_order = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

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
    content = RichTextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_main_slider = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_breaking = models.BooleanField(default=False)
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
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.category.slug, self.seo_slug])
    
    def save(self, *args, **kwargs):
        # Auto-generate SEO title and slug if not provided
        if not self.seo_title:
            self.seo_title = self.title
        if not self.seo_slug:
            self.seo_slug = self.title.lower().replace(' ', '-')
        super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'

class SocialMedia(models.Model):
    facebook = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)
    gmail = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.id)

class WebAddress(models.Model):
    about = models.TextField(blank=True, null=True)        
    address_1 = models.TextField(blank=True, null=True)        
    address_2 = models.TextField(blank=True, null=True)        
    address_3 = models.TextField(blank=True, null=True)        
    state = models.TextField(blank=True, null=True)        
    city = models.TextField(blank=True, null=True)        
    zipcode = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.address_1
        