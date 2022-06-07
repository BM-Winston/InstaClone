from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    
    

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    profile_photo = models.ImageField('profile_photo',blank=True)
    profile_bio = models.TextField()
    

    def __str__(self):
        return self.user.username
