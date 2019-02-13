
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from .forms import LoginForm

def signup_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sherlock:homepage')
    else:
        form=LoginForm(request.POST)
    return render(request,'signup.html',{'form':form})

def homepage(request):
    return HttpResponse("done")

def log_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            return redirect('sherlock:homepage')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
