
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        sign=UserCreationForm(request.POST)
        if sign.is_valid():
            sign.save()
            return redirect('accounts:homepage')
    else:
        sign=UserCreationForm()
    return render(request,'signup.html',{'form':sign})

def log_view(request):
    if request.method=='POST':
        sign=AuthenticationForm(data=request.POST)
        if sign.is_valid():
            user=sign.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:homepage')
    else:
        sign=AuthenticationForm()
    return render(request,'login.html',{'form':sign})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:homepage')

def homepage(request):
    return HttpResponse("Sherlock")
