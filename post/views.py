from django.shortcuts import render,get_object_or_404, redirect
from post.forms import CommentForm
from post.models import *
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import HttpResponseBadRequest

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

def category_detail(request, slug):
    cat_posts = Blog.objects.filter(category__slug=slug)
    cat = get_object_or_404(Category, slug=slug)
    top_three_news = Blog.objects.filter(is_published=True, status='published').order_by('-created_at')[:3]
    
    # Add pagination
    paginator = Paginator(cat_posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,  # Pass the paginated posts
        'cat': cat,
        'top_three_news': top_three_news,
        'paginator': paginator,  # Optional if you want to add extra pagination data in the template
    }
    return render(request, 'category-detail.html', context)

def blog_detail(request, category_slug, blog_slug):
    # Fetch the category by its slug
    category = get_object_or_404(Category, slug=category_slug)
    
    # Fetch the blog post by the category and blog slug
    blog_post = get_object_or_404(Blog, seo_slug=blog_slug, category=category)
    more_news = Blog.objects.filter(status='published').order_by('-created_at')
    # Fetch comments related to the blog post
    comments = Comment.objects.filter(blog=blog_post).order_by('-created_at')

    context = {
        'blog_post': blog_post,
        'category': category,
        'more_news':more_news,
        'comments':comments,
    }
    return render(request, 'blog_detail.html', context)

def post_comment(request, category_slug, blog_slug):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = get_object_or_404(Blog, seo_slug=blog_slug, category__slug=category_slug)
            comment.save()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Your comment has been submitted.'})
            
            return redirect('blog_detail', category_slug=category_slug, blog_slug=blog_slug)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'There was an error with your submission.'}, status=400)
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

    return redirect('blog_detail', category_slug=category_slug, blog_slug=blog_slug)

def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow:",
        "Sitemap: https://elnbc.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def search_blog_posts(request):
    query = request.GET.get('q', '')
    if query:
        results = Blog.objects.filter(Q(title__icontains=query), status='published')
    else:
        results = Blog.objects.all()  # Return no results if query is empty

    html = render_to_string('_search_results.html', {'results': results})
    return JsonResponse({'html': html})