from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm        # django has inbuilt form for user creation
from django.contrib import messages                     # to print msg after,eg.,after login show msg'you are logged in'
from .forms import UserRegisterForm  #imported from forms.py
from django.contrib.auth.decorators import login_required  #decorators required when the user logged in then only user has acces to some files

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')

            messages.success(request,f'your account has been created ,you are now able to login')
            return redirect( 'login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

