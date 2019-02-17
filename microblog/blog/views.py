from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>MicroBlog Home</h1>')

def about_view(request):
    return HttpResponse('<h1>About</h1>')
