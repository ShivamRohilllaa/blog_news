from django.shortcuts import render
from post.models import *
# Create your views here.

def index(request):
    slider_posts = Blog.objects.filter(is_main_slider=True, is_published=True, status='published')
    breaking_news = Blog.objects.filter(is_breaking=True, is_published=True, status='published')
    
    
    context = {'slider_posts':slider_posts, 'breaking_news':breaking_news}
    
    
    return render(request, 'index.html', context)

