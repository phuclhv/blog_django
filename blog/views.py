from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author': 'phuclhv',
    'title': 'First post',
    'date_posted': 'Some content',
    'date_posted': 'Nov 11, 2019'
  },
  {
    'author': 'Jeff Dean',
    'title': 'Second post',
    'date_posted': 'Another content',
    'date_posted': 'Nov 12, 2019'
  }
]
def home(request):
  context = {
    'posts': posts,
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


