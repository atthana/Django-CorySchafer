from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Atthana',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 8, 2020'
    },
    {
        'author': 'Pawan',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 1, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})