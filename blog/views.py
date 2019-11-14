from django.shortcuts import render
from .models import Post

def home(request):
  context = {
    'posts': Post.objects.all(),
    'name': 'Home',
  } 
  # pass information to template
  # return an HTTP respons
  return render(request, 'blog/home.html', context)

def about(request):
  
  context = {
    'title': 'About',
    'name': 'About',
  }
  return render(request, 'blog/about.html', context)


