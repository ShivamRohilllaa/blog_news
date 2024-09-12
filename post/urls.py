from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.category_detail, name='category_detail'),
    path('<str:category_slug>/<str:blog_slug>/', views.blog_detail, name='blog_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)