from django.db import models
from django. contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):  #inherits from Abstractuser model
   profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)  #stores the user profile pic
   bio = models.TextField(blank=True)  #strores the user bio

   def __str__(self):
        return self.username

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')  #when the user deletes the profile the pictures will also be deleted

    def __str__(self):
        return self.title

   