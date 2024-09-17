from django.contrib.sitemaps import Sitemap
from post.models import Category, Blog

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Return all categories
        return Category.objects.all()
    
    def location(self, obj):
        # Use the get_absolute_url method of the model to get the URL
        return obj.get_absolute_url()


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        # Return only published blogs
        return Blog.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()
