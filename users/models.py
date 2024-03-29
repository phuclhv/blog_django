from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) # Cascade means that if we delete a user, we will delete the blog posted by that user but not otherwise
  image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'
    
  def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.image.path)
    img.convert("RGB")

    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)
      




