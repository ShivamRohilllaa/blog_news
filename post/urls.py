from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from post.sitemap import CategorySitemap, BlogSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    # 'static': StaticViewSitemap,
    # 'contact': StaticViewSitemapcontact,
    'category': CategorySitemap,
    'blogs': BlogSitemap,
}
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.category_detail, name='category_detail'),
    path('<str:category_slug>/<str:blog_slug>/', views.blog_detail, name='blog_detail'),
    path('<str:category_slug>/<str:blog_slug>/comment/', views.post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots_txt),
    path('blog/q/search/', views.search_blog_posts, name='search_blog_posts'),
    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)