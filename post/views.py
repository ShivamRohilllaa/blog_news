from django.shortcuts import render
from post.models import *
# Create your views here.

def index(request):
    slider_posts = Blog.objects.filter(is_main_slider=True, is_published=True, status='published')
    breaking_news = Blog.objects.filter(is_breaking=True, is_published=True, status='published')
    top_three_news = Blog.objects.filter(is_published=True, status='published').order_by('-created_at')[:3]
    popular_news = Blog.objects.filter(is_popular=True, status='published')
    international_news = Blog.objects.filter(category__name='International', status='published')
    more_news = Blog.objects.filter(status='published').order_by('-created_at')
    
    context = {'slider_posts':slider_posts, 'breaking_news':breaking_news, 'top_three_news':top_three_news, 'popular_news':popular_news, 'international_news':international_news, 'more_news':more_news}
    
    
    return render(request, 'index.html', context)

