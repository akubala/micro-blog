from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'akubala',
        'title': 'test post 1',
        'content': 'test content 1',
        'date': 'test-date-example'
    },
    {
        'author': 'akubala',
        'title': 'test post 2',
        'content': 'test content 2 ',
        'date': 'test-date-example'
    }
]


def home_view(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about_view(request):
    return render(request, 'blog/about.html')
