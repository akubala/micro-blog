from django.shortcuts import render
from .models import Post


def home_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html')
