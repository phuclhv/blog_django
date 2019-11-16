from django.urls import path
from .views import (
  PostListView, 
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
)
# import . means that import from the current folder
from . import views

urlpatterns = [
  # First parameter to be:wq blank to indicate homepage
  # Make name to be blog-home instead of home because we might have another homepage app in out application
  path('', PostListView.as_view(), name='blog-home'),
  path('about/', views.about, name='blog-about'),
  
  # this path hold a variable, pk means primary key. Pk is the convention for details view
  # <> is the convention for putting a variable for the link
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
