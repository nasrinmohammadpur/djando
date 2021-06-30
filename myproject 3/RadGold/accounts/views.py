
#from django.db.models.expressions import froms
from django.db.models.expressions import F
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .froms import loginfrom
from .models import *

def user_login(request):    
        if request.method == 'POST':   
                form = loginfrom(request.POST)    
                if form.is_valid():    
                        cd = form.cleaned_data    
                        user = authenticate(request,  username=cd['username'],password=cd['password'])    
                        if user is not None:    
                                if user.is_active:    
                                        login(request, user)    
                                        return HttpResponse("احراز هویت با موفقیت انجام شد")    
                                else:    
                                        return HttpResponse("حساب غیرفعال است")    
                        else:   
                                return HttpResponse("کاربری با این اطلاعات وجود ندارد")   
        else:    
                form = LoginForm()    
                return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
        logout(request)
        return redirect('home:home')


def user_profile(request):  
        profile=profile.objects.get(user_id=request.user.id)
        return(request,'accounts/profile.html', {'profile',profile})