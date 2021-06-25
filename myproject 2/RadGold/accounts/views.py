from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
     return render(request, 'account/login.html')



def login(request):
   
    if request.method == 'POST':
      
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
       
        if user is not None:
            auth.login(request, user)
            
            return redirect('allproducts')
        else:
            return render(request, 'account/login.html', {'error':'Invalid Username Or Password'})

    else:
        return render(request, 'account/login.html')     

