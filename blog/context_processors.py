from post.models import *
from django.shortcuts import get_object_or_404
from datetime import datetime


def menu_links(request):
    allcat = Category.objects.all()
    return dict(allcat=allcat)

def top_three_cat(request):
    top_cat = Category.objects.filter(is_top_three=True)
    return dict(top_cat=top_cat)

# def related_posts(request):
#     rel_posts = Post.objects.all().order_by('-date')
#     return dict(rel_posts=rel_posts)

def breaking_news(request):
    b_news = Blog.objects.filter(is_breaking=True)
    return dict(b_news=b_news)

def foot_post(request):
    foot_news = Blog.objects.filter(status='published').order_by('-created_at')[:3]
    return dict(foot_news=foot_news)

# def adsense_adsscripts(request):
#     scripts = adsense_scripts.objects.all()
#     return dict(scripts=scripts)

# def head_scripts(request):
#     headmeta = meta.objects.all()
#     return dict(headmeta=headmeta)

def current_date(request):
    today_date = datetime.now().strftime("%A, %B %d")
    return dict(today_date=today_date)