from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render

from bookings.models import Guest
from home.models import Setting
from user.forms import ProfileUpdateForm, SignUpForm, UserUpdateForm
from user.models import UserProfile


# Create your views here.
@login_required(login_url='/login') # Check login
def index(request):
    setting=Setting.objects.get(pk=1)
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'setting': setting,
               'profile':profile}
    return render(request,'user_profile.html',context)

def login_form(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            return redirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return redirect('/login')
    setting=Setting.objects.get(pk=1)
    context={'setting': setting}
    return render(request,template_name='login_form.html',context=context)

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="users/user.png"
            data.save()
            return redirect('/')
            messages.success(request, 'Your account has been created!')
        else:
            return redirect('/signup')
            messages.warning(request,form.errors)

    form = SignUpForm()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'form': form,
               }
    return render(request, 'signup_form.html', context)

def logout_func(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        setting=Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'setting': setting,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login') # Check login
def booked_rooms(request):
    setting=Setting.objects.get(pk=1)
    current_user = request.user
    rooms=Guest.objects.filter(user_id=current_user.id).order_by('-id')
    print(rooms)
    context={"setting":setting,'rooms':rooms}
    return render(request,'booked_rooms.html',context)

