from urllib.request import Request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from matplotlib.style import context

from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f'haha{username}')
            messages.success(request, f'account created. Log in to acccess')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        uuform = UserUpdateForm(request.POST,instance=request.user)
        puform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uuform.is_valid() and puform.is_valid():
            uuform.save()
            puform.save()
            messages.success(request, f'profile updated')
            return redirect('profile')
    
    else:
        uuform = UserUpdateForm(instance=request.user)
        puform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'uuform' : uuform,
        'puform' : puform
    }
    return render(request, 'users/profile.html',context)


