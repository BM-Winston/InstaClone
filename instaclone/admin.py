from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image, Profile,Comment,Like

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
