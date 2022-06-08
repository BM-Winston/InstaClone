from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image



# Create your views here.


def images(request):
    images= Image.objects.all()
    return render(request, 'index.html',{"images": images})
    
