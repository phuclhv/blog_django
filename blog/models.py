from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# create Post class for Blog app
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE) # when we delete author, all the posts will be deleted 

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    # 'reverse()' will return full path as a string
    return reverse('post-detail', kwargs={'pk':self.pk}) 
    







