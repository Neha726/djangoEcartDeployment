from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def home(request):
    return render(request,'index.html')
    
def register(request):

    if request.method == 'POST':
        email=request.POST['email']
        p = request.POST['upass']
        
        print(email=email,password=p)
        
    else:
       pass

       return render(request,'register.html')

