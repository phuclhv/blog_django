from django.urls import path
# import . means that import from the current folder
from . import views

urlpatterns = [
  # First parameter to be:wq blank to indicate homepage
  # Make name to be blog-home instead of home because we might have another homepage app in out application
  path('', views.home, name='blog-home'),
  path('about/', views.about, name='blog-about')
]