from django.db import models
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)


    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()



    
    

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    profile_photo = models.ImageField('profile_photo',blank=True)
    profile_bio = models.TextField()
    

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile_(self, new_profile):
        self.profile = new_profile
        self.save()


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def update_comment(self, new_comment):
        self.comment = new_comment
        self.save()

class Like(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save_like(self):
        self.save()

    def delete_like(self):
        self.delete()

    def update_like(self, new_like):
        self.like = new_like
        self.save()