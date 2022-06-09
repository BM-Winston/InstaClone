from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Image
from instaclone.forms import RegisterForm



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


    
