from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from PIL import Image

class CustomUser(AbstractUser):
    
    bio = models.TextField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def get_absolute_url(self):
    	return reverse('home')

    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)

    	img = Image.open(self.image.path)

    	if img.height > 300 or img.width > 300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)

    def __str__(self):
        return self.username
