from django.shortcuts import redirect, render
from .models import Image
from instaclone.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
import email
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User,Image,Comment,Like,Follow
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


def images(request):
    images= Image.objects.all()
    return render(request, 'index.html',{"images": images})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()   

        return redirect('login')
    else:    
        form = RegisterForm()
    return render(request,'registration/signup.html',{'form':form})

@csrf_exempt
def login(request):
    if request.method == 'POST':
       
        return redirect('images')

   
    return render(request,'registration/login.html')


    
