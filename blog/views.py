from django.shortcuts import render
# LoginRequiredMin forces user to login before creating a blog
# UserPassesTestMixin make user only allow user to change their own posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
  ListView, 
  DetailView,
  CreateView,
  UpdateView
  #DeleteView
)
from django.views.generic.edit import DeleteView
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


# view all posts
class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html' # <app><model>_<viewtype>.html
  context_object_name = 'posts' 
  ordering = ['-date_posted'] # change order to have the newest on Top

# view only one post 
class PostDetailView(DetailView):
  model = Post

class PostCreateView(LoginRequiredMixin, CreateView ):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False









