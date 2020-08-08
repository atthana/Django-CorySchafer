from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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
        'posts': Post.objects.all()  # ค่าในหน้า home มาจาก query all ตรงนี้ล่ะนะ
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})