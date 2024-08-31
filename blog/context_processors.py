from post.models import *
from django.shortcuts import get_object_or_404

def menu_links(request):
    allcat = Category.objects.all()
    return dict(allcat=allcat)

# def related_posts(request):
#     rel_posts = Post.objects.all().order_by('-date')
#     return dict(rel_posts=rel_posts)

def breaking_news(request):
    b_news = Blog.objects.filter(is_breaking=True)
    return dict(b_news=b_news)

# def adsense_adsscripts(request):
#     scripts = adsense_scripts.objects.all()
#     return dict(scripts=scripts)

# def head_scripts(request):
#     headmeta = meta.objects.all()
#     return dict(headmeta=headmeta)