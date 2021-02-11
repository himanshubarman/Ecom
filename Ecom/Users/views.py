from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'Users/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!.Now you can login to your account')
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request,'Users/register.html',{'form': form})

def login_view(request):
    if request.method:
        form = LoginForm(request.POST)
        if form.is_valid():
            cleandata = form.cleaned_data

            user = authenticate(username=cleandata['username'],password=cleandata['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,f'Logged In successfully for {user.username}!.')
                    return redirect('home')
                else:
                    messages.warning(request, f'{user.username} is not active!.')
                    return redirect('login')
            else:
                messages.warning(request,'Username or password did not matched')
                return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'Users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request,"You logged out successfully")
    return redirect('login')



