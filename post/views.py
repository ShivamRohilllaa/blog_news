from django.shortcuts import render
from post.models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

